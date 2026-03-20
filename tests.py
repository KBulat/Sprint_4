import pytest
from main import BooksCollector
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.skip(reason="Пример теста")
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
    
        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    @pytest.mark.parametrize('book_name', [
        'N', 
        'N' * 20,
        'N' * 40,
        'N' * 41,
        '', 
    ])
    def test_add_new_book_different_name_lengths_added_if_valid(self, book_name, collector):
        collector.add_new_book(book_name)

        is_valid = 0 < len(book_name) < 41
        assert (book_name in collector.get_books_genre()) == is_valid

    def test_set_book_genre_valid_genre_book_genre_set(self, collector):
        collector.add_new_book('Человек-амфибия')
        collector.set_book_genre('Человек-амфибия', 'Фантастика')

        assert collector.get_book_genre('Человек-амфибия') == 'Фантастика'
    
   
    @pytest.mark.parametrize(
        'book_name, book_genre', 
        [
            ('Фантастические истории', 'Фантастика'),
            ('Ужасающие истории', 'Ужасы'),
            ('Детективные истории', 'Детективы'),
            ('Мультипликационные истории', 'Мультфильмы'),
            ('Комедийные истории', 'Комедии')
        ]                                
    )
    def test_get_book_genre_book_with_genre_returns_genre(self, collector, book_name, book_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_valid_genre_returns_books(self, collector):
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.add_new_book('Имя Розы')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.set_book_genre('Имя Розы', 'Детективы')

        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_genre_returnes_dict(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}
    
    def test_get_books_for_children_age_restricted_genres_not_included(self, collector):
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        assert 'Дракула' not in collector.get_books_for_children()

    def test_get_books_for_children_allowed_genres_included(self, collector):
        collector.add_new_book('Приключения Электроника')   
        collector.set_book_genre('Приключения Электроника', 'Фантастика')
        
        assert 'Приключения Электроника' in collector.get_books_for_children()

    def test_add_book_in_favorites_book_in_collection_added_to_list(self, collector):
        collector.add_new_book('Человек-невидимка')
        collector.add_book_in_favorites('Человек-невидимка')

        assert 'Человек-невидимка' in collector.get_list_of_favorites_books()     

    def test_delete_book_from_favorites_book_in_favorites_removed_from_list(self, collector):
        collector.add_new_book('Шантарам')
        collector.add_book_in_favorites('Шантарам')
        collector.delete_book_from_favorites('Шантарам')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_books_not_in_collection_not_returned(self, collector):
        collector.add_book_in_favorites('Сумерки')

        assert 'Сумерки' not in collector.get_list_of_favorites_books()
