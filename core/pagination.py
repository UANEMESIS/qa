from rest_framework.pagination import (LimitOffsetPagination, PageNumberPagination,)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 2
	page_query_param = 'num'
	max_limit = 4