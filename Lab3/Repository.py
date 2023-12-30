"""!
@file Repository.py
@brief Основной файл класса репозитория
@date 2023.10.17
@author Пакало А.С. ИУ5-12М

Хранит в себе определение класса репозитория для анализа GitHub.
"""

"""!
@package docstring
Модуль репозитория.
 
Используется для упрощения анализа репозиториев GitHub, абстрагируя основные функции в классе.
"""
 
class Repository:
    """!
    @brief Отвечает за обработку репозитория.
 
    Позволяет манипулировать основными данными о репозитории.
    """

    def __init__(self, owner, url):
        """!
        @brief Конструктор класса Repository
        
        Требует основные данные о проекте

        @param owner Владелец репозитория
        @param url Ссылка на репозиторий
        @return класс Repository
        """
        ## Владелец репозитория
        self._owner = owner
        ## Ссылка на репозиторий
        self._url = url
   
    def changeUrl(self, url):
        """!
        @brief Изменить ссылку репозитория
        
        Изменить поле url у соответствующего репозитория. Влияет на отображение в хостинге.

        @param url Ссылка на репозиторий
        @return изменённая ссылка - новая ссылка на данный репозиторий
        """
        self._url = url

    def changeOwner(self, owner):
        """!
        @param owner Владелец репозитория
        Изменить владельца репозитория

        @throw UserException - Такого пользователя не существует.
        @return изменённый пользователь - новый владелец репозитория
        """
        self._owner = owner


class GitHubRepository extends Repository:
    """!
    @brief Отвечает за обработку репозитория GitHub.
 
    Позволяет манипулировать основными данными о репозитории GitHub.
    """
   
    def __init__(self, owner, url):
        """!
        @brief Конструктор класса GitHubRepository

        Требует основные данные о проекте

        @throw Exception - Ошибка при создании GitHub репозитория.
        @return класс GitHubRepository
        """
        super().__init__(owner, url)
        ## Ссылки на обсуждения GitHub.
        self._issues = issues

    def changeIssues(self, issues):
        """!@brief Изменение issues для данного репозитория

        Позволяет изменить набор issue - предложений или обсуждений багов и потенциальных улучшений проекта.
        @throw IssueException - Такого обсуждения не существует.

        @return итоговый набор issue
        """
        self._issues = issues

        return self._issues

    def addIssue(self, issue):
        """!Пример использования addIssue
        @code
        gitHubRepository = GitHubRepository()
        gitHubRepository.addIssue(issue)
        @endcode

        @throw IssueException - Такого обсуждения не существует.

        @return итоговый набор issue
        """
        self._issues.append(issue)

        return self._issues

