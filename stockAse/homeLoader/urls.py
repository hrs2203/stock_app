from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import urls
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.welcomePage, name="welcome"),

    path('company/<int:id>', views.companyPage, name='company_page'),
    path('company/new', views.newCompany, name='new_company'),
    path('company/shares/<int:id>', views.editCompanyShares, name='edit_shares'),

    path('user', views.userPage, name='user'),
    path('user/companies', views.myCompanies, name='user_companies'),
    path('user/shares/<int:id>', views.sellMyShares, name='sell_shares'),
    path('user/buy/shares/<int:id>', views.buyShares, name='buy_shares'),
    path('user/payment/<int:id>', views.simulateTransaction, name='payment'),
    path('user/payment/start/<int:id>',
         views.startTransaction, name='transaction'),
    path('user/transactions', views.myTransactions, name='user_transactions'),
    path('user/wishlist/', views.myWishList, name='wish_list'),
    path('user/wishlist/add/<int:id>',
         views.addToWishList, name='add_to_wish_list'),
    path('user/wishlist/remove/<int:id>',
         views.removeFromWishList, name='remove_from_wish_list'),

    path('friend/<int:id>', views.friendPage, name='view_friend'),

    path('market', views.market, name='market'),
    path('shares', views.myShares, name='view_shares'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),
    url(r'^log_out/$', views.log_out, name='log_out'),

    path('sample/test_data', views.send_testGraphData),
    path('company/data/<str:compCode>/<str:compKey>', views.getCompLiveData),
    path('company/cached_data/<str:compCode>/<str:compKey>',
         views.getCachedCompanyStockData),
    path('exploreCompany', views.exploreCompany, name='exploreCompany'),
]
