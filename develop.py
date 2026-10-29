import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collect):
        collect.add_new_book('Война и мир')
        collect.add_new_book('Преступление и наказание')
        assert len(collect.get_books_genre()) == 2, 'Книги не добавились'

    @pytest.mark.parametrize('book_names', ['', 'Очень_длинное_название_книги_на_сорок_один_с', 
                                            'Очень_длинное_название_книги_на_сорок_два_симв'])
    def test_add_new_book_add_negative_book(self, collect, book_names):
        collect.add_new_book(book_names)
        assert len(collect.get_books_genre()) == 0, 'Проверка условия метода не пройдена, книга добавилась'

    def test_set_book_genre_added_genre_book_positive_result(self, collect):
        collect.add_new_book('Убийство в Восточном экспрессе')
        collect.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collect.books_genre.get('Убийство в Восточном экспрессе') == 'Детективы'

    def test_set_book_genre_add_genre_is_not_list(self, collect):
        collect.add_new_book('Убийство в Восточном экспрессе')
        collect.set_book_genre('Убийство в Восточном экспрессе', 'Фантастика')
        assert collect.books_genre.get('Убийство в Восточном экспрессе') == '', 'Книге добавился жанр которого нет в допустимых жанрах'

    def test_get_book_genre_for_name_positive_result(self, collect):
        collect.add_new_book('Убийство в Восточном экспрессе')
        collect.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collect.get_book_genre('Убийство в Восточном экспрессе') == 'Детективы'

    def test_get_books_with_specific_genre_get_two_books_detectiv(self, collect):
        collect.books_genre = {'Детектив 1': 'Детективы', 'Детектив 2': 'Детективы', 'Страшилка': 'Ужасы',
                               'Мультик': 'Мультфильмы'}
        assert len(collect.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_for_children_two_books(self, collect):
        collect.books_genre = {'Мультик 1': 'Мультфильмы', 'Детектив': 'Детективы', 'Страшилка': 'Ужасы',
                               'Смешинка': 'Комедии'}
        assert len(collect.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collect):
        collect.add_new_book('Мастер и Маргарита')
        collect.add_book_in_favorites('Мастер и Маргарита')
        assert len(collect.get_list_of_favorites_books()) == 1 and collect.favorites[0] == 'Мастер и Маргарита'

    def test_add_book_in_favorites_add_two_double_book(self, collect):
        collect.add_new_book('Мастер и Маргарита')
        collect.add_book_in_favorites('Мастер и Маргарита')
        collect.add_book_in_favorites('Мастер и Маргарита')
        assert len(collect.get_list_of_favorites_books()) == 1, 'В избранное добавился дубль книги'

    def test_delete_book_from_favorites(self, collect):
        collect.add_new_book('Мастер и Маргарита')
        collect.add_book_in_favorites('Мастер и Маргарита')
        collect.delete_book_from_favorites('Мастер и Маргарита')
        assert len(collect.favorites) == 0
