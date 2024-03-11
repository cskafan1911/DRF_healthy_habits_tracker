from rest_framework.pagination import PageNumberPagination


class HabitsPaginator(PageNumberPagination):
    """
    Класс для пагинации вывода списка привычек текущего пользователя.
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
