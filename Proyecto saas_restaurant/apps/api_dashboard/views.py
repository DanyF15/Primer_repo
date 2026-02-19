from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.api_users.permissions import IsRestaurantAdmin
from apps.api_order.models import OrderDetail
from apps.api_menu.models import Dish

class DashboardTopDishesView(APIView):
    permission_classes = [IsAuthenticated, IsRestaurantAdmin]

    def get(self, request):
        current_restaurant = request.user.employee_profile.restaurant
        
        top_dishes_qs = OrderDetail.objects.filter(
            order__session__table__restaurant=current_restaurant,
            order__status='CERRADA'
        ).values('dish__name').annotate(
            total_sold=Sum('quantity')
        ).order_by('-total_sold')[:5]

        data = [
            {"name": item['dish__name'], "value": item['total_sold']}
            for item in top_dishes_qs
        ]

        return Response(data)

class DishPerformanceView(APIView):
    permission_classes = [IsAuthenticated, IsRestaurantAdmin]

    def get(self, request, dish_id):
        current_restaurant = request.user.employee_profile.restaurant
        
        dish = get_object_or_404(Dish, id=dish_id, restaurant=current_restaurant)

        details_qs = OrderDetail.objects.filter(
            dish=dish,
            order__status='CERRADA' 
        )

        total_sold = details_qs.aggregate(total=Sum('quantity'))['total'] or 0

        monthly_stats = (
            details_qs
            .annotate(month=TruncMonth('order__created_at'))
            .values('month')
            .annotate(count=Sum('quantity'))
            .order_by('month')
        )

        history_data = [
            {
                "month": stat['month'].strftime('%Y-%m-%d'),
                "quantity": stat['count']
            }
            for stat in monthly_stats
        ]

        return Response({
            "dish_info": {
                "name": dish.name,
                "category": dish.category.name if dish.category else "Sin categoría",
                "current_price": dish.price,
                "is_active": dish.is_active
            },
            "total_sold_all_time": total_sold,
            "sales_history": history_data
        })

class MonthlyRevenueView(APIView):
    permission_classes = [IsAuthenticated, IsRestaurantAdmin]

    def get(self, request):
        current_restaurant = request.user.employee_profile.restaurant
        
        now = timezone.now()
        year = int(request.query_params.get('year', now.year))
        month = int(request.query_params.get('month', now.month))

        monthly_sales = OrderDetail.objects.filter(
            order__session__table__restaurant=current_restaurant,
            order__status='CERRADA',
            order__created_at__year=year,
            order__created_at__month=month
        )

        stats = monthly_sales.aggregate(
            total_revenue=Sum(F('unit_price') * F('quantity')),
            total_dishes_sold=Sum('quantity')
        )

        return Response({
            "period": f"{month}/{year}",
            "total_revenue": stats['total_revenue'] or 0.00,
            "total_dishes_sold": stats['total_dishes_sold'] or 0
        })