from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'blog'

# URLパターンを登録するための変数
urlpatterns = [
    # リクエストされたURLが''(無し)の場合
    # viewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
]
