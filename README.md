<h2>Описание проекта</h2>
На главной странице приложения можно ввести свое имя.<br>
Если имя было введено раньше, программа выведет сообщение о том, что это имя уже было использовано.<br>
Если имя встретилось впервые, программа поприветствует пользователя.<br>
<br>
Веб приложение написано на фреймворке Flask. База данных SQLite.<br>
Проект хостится на heroku: https://evo-test-appp.herokuapp.com/
<h2>Запуск приложения на Windows:</h2>
  <h3>1. Клонировать репозиторий на компьютер:</h3>
      <ul>
       <li>Создать папку, открыть консоль и пройти в эту папку с помощью команды cd.</li>
         Например: <b>cd C:\app_directory </b>
       <li>В консоли ввести команду:</li>
         <b>-git clone https://github.com/Alexander-Igonin/evo_task_2.git </b>
      </ul>
 <h3>2. Установить виртуальное окружение Python:</h3>
      <ul>
        <li> Зайти в папку проекта и ввести в консоли:</li>
         <b>python -m venv env</b>
        <li> Активировать виртуальное окружение:</li>
          <b>venv/Scripts/activate</b>
        <li> Установить нужные библиотеки</li>
         <b>pip install -r requirements.txt</b>
      </ul>
<h3>3.  Запуск приложения:</h3>
   <ul>
    <li> Запустить файл main.py </li>
    <li> В браузере перейти по адресу http://127.0.0.1:5000/ </li>
   </ul>
