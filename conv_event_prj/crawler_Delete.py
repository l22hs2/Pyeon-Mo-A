import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conv_event_prj.settings')
import django
django.setup()
from web.models import Product

# 오늘 날짜 변수에 저장
today = datetime.date.today()
count = 0

# 오늘 날짜가 아닌(행사 종료) 상품 조회
products = Product.objects.exclude(created_at = today)

# 행사 종료 상품이면 제거
if products:
    for p in products:
        p.delete()
        count += 1
    print(f"{count}개 상품 삭제 완료")
else:
    print("대상이 존재하지 않습니다")
