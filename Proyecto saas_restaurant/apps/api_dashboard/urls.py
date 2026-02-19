from django.urls import path
from .views import DashboardTopDishesView, DishPerformanceView, MonthlyRevenueView

urlpatterns = [
    path('top-dishes/', DashboardTopDishesView.as_view(), name='dashboard_top_dishes'),

    # Métricas financieras del mes 
    path('monthly-revenue/', MonthlyRevenueView.as_view(), name='dashboard_monthly_revenue'),

    # Detalle de rendimiento de un plato específico
    path('dish-performance/<int:dish_id>/', DishPerformanceView.as_view(), name='dashboard_dish_performance'),
]