from django.urls import path
from .views import index,user_home,create,new,detail,update,delete,user_sign_up,co_home,co_sign_up,co_create,co_detail,user_detail,co_mypage
urlpatterns = [
    path('create/', create, name="create"), #create는 Memo와 관련된 기능이므로 Memo 앱 안에서 관리해주겠습니다.
    path('new/', new, name="new"),
    path('detail/<int:detail_id>', detail, name="detail"), #주소창의 URL뒤에 detail/5 라고 붙게 될시 5라는 요소를 int속성으로 detail_id라는 이름으로 지정한다는 의미.
    path('update/<int:update_id>', update, name="update"), #path converter(<int:update_id>)에 붙이는 이름은 자유롭게 붙이셔도 상관없지만 일반적으로는 pk를 많이 씁니다.
    path('delete/<int:delete_id>', delete, name="delete"),
    path('user_home/', user_home, name="user_home"), 
    path('user_sign_up/', user_sign_up, name="user_sign_up"),
    path('co_home/', co_home, name="co_home"),
    path('co_sign_up/', co_sign_up, name="co_sign_up"),
    path('co_create/', co_create, name="co_create"),
    path('co_detail/<int:co_detail_id>', co_detail, name="co_detail"),
    path('user_detail/<int:user_detail_id>', user_detail, name="user_detail"),
    path('co_mypage/', co_mypage, name="co_mypage"),

]

