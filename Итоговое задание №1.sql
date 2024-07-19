--Создание таблицы для хранения фамилий
CREATE TABLE
  last_name (id serial PRIMARY key, last_name text);

--Создание таблицы для хранения имен
CREATE TABLE
  first_name (id serial PRIMARY key, first_name text);

--Создание таблицы для хранения отчеств
CREATE TABLE
  middle_name (id serial PRIMARY key, middle_name text);

--Заполнение данными таблицы с фамилиями
INSERT INTO
  last_name (last_name)
VALUES
  ('Иванов'),
  ('Петров'),
  ('Сидоров');

--Заполнение данными таблицы с именами
INSERT INTO
  first_name (first_name)
VALUES
  ('Иван'),
  ('Петр'),
  ('Сидор');

--Заполнение данными таблицы с отчествами
INSERT INTO
  middle_name (middle_name)
VALUES
  ('Иванович'),
  ('Петрович'),
  ('Сидорович');

--Запрос на возвращения трех Ф.И.О. целиком в обратном алфавитном порядке
SELECT
  ln2.last_name||' '||fn.first_name||' '||mn.middle_name AS "Ф.И.О"
FROM
  last_name ln2
  JOIN first_name fn ON ln2.id=fn.id
  JOIN middle_name mn ON ln2.id=mn.id
ORDER BY
  "Ф.И.О." desc;
