# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Book:
    """
    Класс, хранящий данные о книге.

    >>> book = Book("1884", "Приключения Гекльберри Финна", 279)
    >>> book.title
    '1884'

    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        :raises TypeError: Если pages не является целым числом.
        :raises ValueError: Если pages меньше или равно нулю.
        """
        self.title = title
        self.author = author
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.pages = pages

    def read(self, pages_to_read: int) -> None:
        """
        Читает заданное количество страниц книги.

        :param pages_to_read: Количество страниц, которые нужно прочитать.
        :raises TypeError: Если pages_to_read не является целым числом.
        :raises ValueError: Если pages_to_read отрицательный или больше общего числа страниц.

        >>> book = Book("1884", "Приключения Гекльберри Финна", 279)
        >>> book.read(50)
        """
        if not isinstance(pages_to_read, int):
            raise TypeError("Количество страниц для чтения должно быть целым числом.")
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным.")
        if pages_to_read > self.pages:
            raise ValueError("Нельзя прочитать больше страниц, чем есть в книге.")
        ...

    def add_bookmark(self, page: int) -> None:
        """
        Добавляет закладку на определенную страницу.

        :param page: Номер страницы, на которую нужно добавить закладку.
        :raises TypeError: Если page не является целым числом.
        :raises ValueError: Если page отрицательный или не попадает в диапазон страниц книги.

        >>> book = Book("1884", "Приключения Гекльберри Финна", 279)
        >>> book.add_bookmark(100)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть целым числом.")
        if page <= 0:
            raise ValueError("Номер страницы должен быть положительным.")
        if page <= 0 or page > self.pages:
            raise ValueError("Номер страницы должен быть в диапазоне от 1 до количества страниц книги.")
        ...

    def close(self) -> None:
        """
        Закрывает книгу.

        >>> book = Book("1884", "Приключения Гекльберри Финна", 279)
        >>> book.close()
        """
        ...

class Table:
    """
    Класс, описывающий стол.

    >>> table = Table("круглый", "желтый", 1.2)
    >>> table.shape
    'круглый'

    """
    def __init__(self, shape: str, color: str, size: float):
        """
        Создание объекта "Стол".

        :param shape: Форма стола (например, "круглый", "прямоугольный").
        :param color: Цвет стола (например, "желтый", "красный").
        :param size: Размер стола (в метрах, положительное число).
        :raises ValueError: Если размер <= 0.
        :raises TypeError: Если размер стола не является числом

        """

        if not isinstance(size, (int, float)):
             raise TypeError("Размер стола должен быть числом")
        if size <= 0:
            raise ValueError("Размер стола должен быть больше 0")
        self.shape = shape
        self.color = color
        self.size = size

    def resize(self, new_size: float) -> None:
        """
        Изменить размер стола.

        :param new_size: Новый размер стола (положительное число).
        :raises ValueError: Если новый размер <= 0.
        :raises TypeError: Если новый размер стола не является числом

        >>> table = Table("круглый", "желтый", 1.2)
        >>> table.resize(2.0)
        """
        if not isinstance(new_size, (int, float)):
             raise TypeError("Новый размер стола должен быть числом")
        if new_size <= 0:
            raise ValueError("Новый размер должен быть больше 0.")
        ...

    def change_color(self, new_color: str) -> None:
        """
        Покрасить стол в новый цвет.

        :param new_color: Название нового цвета (например, "белый").
        >>> table = Table("круглый", "желтый", 2.0)
        >>> table.change_color("белый")
        """
        ...

    def extend_surface(self, additional_size: float) -> None:
        """
        Увеличить площадь стола, добавив дополнительный участок поверхности.

        :param additional_size: Размер дополнительной поверхности (в метрах, положительное число).
        :raises ValueError: Если размер <= 0.
        :raises TypeError: Если размер дополнительной поверхности стола не является числом

        >>> table = Table("прямоугольный", "желтый", 1.2)
        >>> table.extend_surface(0.5)
        """
        if not isinstance(additional_size, (int, float)):
             raise TypeError("Размер дополнительной поверхности стола должен быть числом")
        if additional_size <= 0:
            raise ValueError("Размер дополнительной поверхности должен быть больше 0.")
        ...


class MusicAlbum:
    """
    Класс, описывающий музыкальный альбом.

    >>> album = MusicAlbum("ТРУДНЫЙ ВОЗРАСТ", "МакSим", ["Ветром стать", "Знаешь ли ты"])
    >>> album.title
    'Abbey Road'

    """
    def __init__(self, title: str, artist: str, tracks: list[str]):
        """
        Создание объекта "Музыкальный Альбом".

        :param title: Название альбома.
        :param artist: Исполнитель.
        :param tracks: Список треков.
        :raises ValueError: Если tracks пустой.
        """
        if not tracks:
            raise ValueError("Список треков не может быть пустым.")
        self.title = title
        self.artist = artist
        self.tracks = tracks

    def add_track(self, track_name: str) -> None:
        """
        Добавить трек в альбом.

        :param track_name: Название трека.
        :raises ValueError: Если трек уже существует.

        >>> album = MusicAlbum("ТРУДНЫЙ ВОЗРАСТ", "МакSим", ["Ветром стать", "Знаешь ли ты"])
        >>> album.add_track("Сон")
        """
        if track_name in self.tracks:
            raise ValueError("Трек уже существует.")
        ...

    def remove_track(self, track_name: str) -> None:
        """
        Удалить трек из альбома.

        :param track_name: Название трека для удаления.
        :raises ValueError: Если трек не найден.

        >>> album = MusicAlbum("ТРУДНЫЙ ВОЗРАСТ", "МакSим", ["Ветром стать", "Знаешь ли ты"])
        >>> album.remove_track("Сон")
        """
        if track_name not in self.tracks:
            raise ValueError("Трек не найден.")
        ...

    def get_tracklist(self) -> list[str]:
        """
        Получить список треков.

        >>> album = MusicAlbum("ТРУДНЫЙ ВОЗРАСТ", "МакSим", ["Ветром стать", "Знаешь ли ты"])
        >>> album.get_tracklist()
        """
        return self.tracks


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
