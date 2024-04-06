### Организуйте систему учёта для питомника, в котором живут домашние и вьючные животные. 
Используя команду cat в терминале операционной системы Linux, создать два файла Домашние животные (заполнив файл собаками, кошками, хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и ослы), а затем объединить их.

## Практическое задание для итоговой аттестации
Итоговая контрольная работа
Информация о проекте
Необходимо организовать систему учета для питомника в котором живут
домашние и вьючные животные.
### Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный репозиторий(Github, gitlub, или Bitbucket). Разработку вести в этом репозитории, использовать пул реквесты на изменения. 
Программа должна запускаться и работать, ошибок при выполнении программы быть не должно.
Программа, может использоваться в различных системах, поэтому необходимо разработать класс в виде конструктора

# Решение

### 1. Используя команду cat в терминале операционной системы Linux, создать два файла Домашние животные (заполнив файл собаками, кошками, хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и ослы), а затем объединить их. Просмотреть содержимое созданного файла. Переименовать файл, дав ему новое имя (Друзья человека).

Выполнениие команды:

``` ruby
cat > "Домашние животные.txt"
cat > "Вьючные животные.txt"
cat "Домашние животные.txt" "Вьючные животные.txt" > "Друзья человека.txt"
cat "Друзья человека.txt"
```
![2024-03-30_16-18-37](https://github.com/Vlad100001/-/assets/132137476/54bbafe0-990d-4341-9cd2-95596804ea05)
![2024-03-30_16-49-25](https://github.com/Vlad100001/-/assets/132137476/b73c2c5b-6647-4822-9c1d-f2a445ecdae1)


```ruby
mv  "Друзья человека.txt"  "Друзья_человека.txt"
```
![2024-03-30_16-54-02](https://github.com/Vlad100001/-/assets/132137476/47ff41e1-ee3e-4105-9d1c-588d495ad184)


### 2. Создать директорию, переместить файл туда.

```ruby
 $ mkdir animal
 $ mv "Друзья_человека.txt" animal/
```
![2024-03-30_20-11-04](https://github.com/Vlad100001/-/assets/132137476/44f489e3-1d15-482e-8c88-7bb191ccd4fa)

### 3. Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория.

```ruby
wget https://dev.mysql.com/get/mysql-apt-config_0.8.18-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.18-1_all.deb
```
![2024-03-30_20-30-07](https://github.com/Vlad100001/-/assets/132137476/8e6284ff-f2fb-41c7-8408-db5871c99ddf)

```ruby
apt update
apt install mysql-server
```
![2024-03-30_20-40-36](https://github.com/Vlad100001/-/assets/132137476/48754d84-1d46-4d8d-a1b1-595b8dfe47b7)

### 4. Установить и удалить deb-пакет с помощью dpkg.
```ruby
wget https://dev.mysql.com/get/mysql-apt-config_0.8.18-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.18-1_all.deb
sudo dpkg -r mysql-apt-config
```
![2024-03-30_21-13-13](https://github.com/Vlad100001/-/assets/132137476/6e93e712-1b74-49a2-90c4-923dce513898)

### 5. Выложить историю команд в терминале ubuntu
```ruby
history
```
![2024-04-02_22-41-42](https://github.com/Vlad100001/-/assets/132137476/5b391082-ea59-4e31-9521-6862b78d5a74)

### 6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние животные и вьючные животные, в составы которых в случае домашних животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные войдут: Лошади, верблюды и ослы).

![diagram](https://github.com/Vlad100001/-/assets/132137476/7711038d-9c48-42bb-8786-9e99a3ea9b99)

### 7. В подключенном MySQL репозитории создать базу данных “Друзья человека”
```ruby
DROP DATABASE IF EXISTS `friends_man`;

CREATE DATABASE IF NOT EXISTS `friends_man`;
```

### 8. Создать таблицы с иерархией из диаграммы в БД

```ruby
USE friends_man;

CREATE TABLE `animals` (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
  animals_class VARCHAR(30)
);

CREATE TABLE `cats` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`animal_class_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
);

CREATE TABLE `dogs` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`animal_class_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
);

CREATE TABLE `hamsters` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`animal_class_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
);

CREATE TABLE `horses` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`animal_class_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
);

CREATE TABLE `camels` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`animal_class_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
);

CREATE TABLE `donkeys` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`animal_class_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
);

```

### 9. Заполнить низкоуровневые таблицы именами(животных), командами которые они выполняют и датами рождения

```ruby

INSERT INTO `friends_man`.`animals` (`id`, `animals_class`) 
VALUES ('1', 'pet'),
	('2', 'wild');

INSERT INTO `friends_man`.`dogs` (`name`, `skills`, `birth_date`, `animal_class_id`) 
VALUES ('Полкан', 'Голос', '2019-05-01', 1),
	('Макс', 'Прыжок через барьер', '2015-06-20', 1);

INSERT INTO `friends_man`.`cats` (`name`, `skills`, `birth_date`, `animal_class_id`) 
VALUES ('Барсик', 'Ловить мышей', '2021-10-10', 1),
	('Матроскин', 'Ловить птиц','2020-05-10', 1);
  
INSERT INTO `friends_man`.`hamsters` (`name`, `skills`, `birth_date`, `animal_class_id`) 
VALUES ('Борька', 'Бегать в колесе', '2022-01-10', 1),
	('Тихон','Строить дом', '2021-05-10', 1);

INSERT INTO `friends_man`.`horses` (`name`, `skills`, `birth_date`, `animal_class_id`) 
VALUES ('Торнадо', 'Горцевать', '2015-01-28', 2),
	('Злотовласка', 'Прыгать через барьеры','2020-04-19', 2);

INSERT INTO `friends_man`.`camels` (`name`, `skills`, `birth_date`, `animal_class_id`) 
VALUES ('Горбушка', 'Прыгать', '2015-01-28', 2),
       ('Рыжик', 'Бегать','2020-04-19', 2);
  
INSERT INTO `friends_man`.`donkeys` (`name`, `skills`, `birth_date`, `animal_class_id`) 
VALUES  ('Упрямыш', 'Есть малину', '2015-01-28', 2),
        ('Метеор', 'Кувыркаться','2020-04-19', 2);
  
```

### 10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

```ruby
INSERT INTO `horses_and_donkeys` (`name`, `skills`, `birth_date`, `animal_class_id`, `species`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'Horse' AS `species`
FROM `horses`;

INSERT INTO `horses_and_donkeys` (`name`, `skills`, `birth_date`, `animal_class_id`, `species`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'Donkey' AS `species`
FROM `donkeys`;

```

### 11.Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице 

```ruby
CREATE TABLE `young_animals` (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(40) NOT NULL,
  `species` VARCHAR(20) NOT NULL,
  `age_months` INT NOT NULL
);

INSERT INTO `young_animals` (`name`, `species`, `age_months`)
SELECT `name`, 
'Dog' AS `species`, 
TIMESTAMPDIFF(MONTH, `birth_date`, CURDATE()) AS `age_months`
FROM `dogs`
WHERE `birth_date` <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND `birth_date` >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR);

INSERT INTO `young_animals` (`name`, `species`, `age_months`)
SELECT `name`, 
'Cat' AS `species`, 
TIMESTAMPDIFF(MONTH, `birth_date`, CURDATE()) AS `age_months`
FROM `cats`
WHERE `birth_date` <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND `birth_date` >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR);

INSERT INTO `young_animals` (`name`, `species`, `age_months`)
SELECT `name`, 
'Donkey' AS `species`, 
TIMESTAMPDIFF(MONTH, `birth_date`, CURDATE()) AS `age_months`
FROM `donkeys`
WHERE `birth_date` <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND `birth_date` >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR);

INSERT INTO `young_animals` (`name`, `species`, `age_months`)
SELECT `name`, 
'Hamster' AS `species`, 
TIMESTAMPDIFF(MONTH, `birth_date`, CURDATE()) AS `age_months`
FROM `hamsters`
WHERE `birth_date` <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND `birth_date` >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR);

INSERT INTO `young_animals` (`name`, `species`, `age_months`)
SELECT `name`, 
'Horse' AS `species`, 
TIMESTAMPDIFF(MONTH, `birth_date`, CURDATE()) AS `age_months`
FROM `horses`
WHERE `birth_date` <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND `birth_date` >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR);

```

### 12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам.

```ruby
CREATE TABLE `all_animals` (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `name` VARCHAR(40) NOT NULL,
  `skills` VARCHAR(100) NOT NULL,
  `birth_date` DATE NOT NULL,
  `animal_class_id` INT UNSIGNED NOT NULL,
  `source_table` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `all_animals` (`name`, `skills`, `birth_date`, `animal_class_id`, `source_table`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'dogs' AS `source_table`
FROM `dogs`;

INSERT INTO `all_animals` (`name`, `skills`, `birth_date`, `animal_class_id`, `source_table`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'cats' AS `source_table`
FROM `cats`;

INSERT INTO `all_animals` (`name`, `skills`, `birth_date`, `animal_class_id`, `source_table`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'donkeys' AS `source_table`
FROM `donkeys`;

INSERT INTO `all_animals` (`name`, `skills`, `birth_date`, `animal_class_id`, `source_table`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'hamsters' AS `source_table`
FROM `hamsters`;

INSERT INTO `all_animals` (`name`, `skills`, `birth_date`, `animal_class_id`, `source_table`)
SELECT `name`, `skills`, `birth_date`, `animal_class_id`,
'horses' AS `source_table`
FROM `horses`;

```

### 13.Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

```ruby

```

### 14. Написать программу, имитирующую работу реестра домашних животных. В программе должен быть реализован следующий функционал:

#### 14.1 Завести новое животное

#### 14.2 определять животное в правильный класс

#### 14.3 увидеть список команд, которое выполняет животное

#### 14.4 обучить животное новым командам

#### 14.5 Реализовать навигацию по меню

### 15.Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆ значение внутренней̆  int переменной̆ на 1 при нажатие “Завести новое животное”.
Сделайте так, чтобы с объектом такого типа можно было работать в блоке try-with-resources. 
Нужно бросить исключение, если работа с объектом типа счетчик была не в ресурсном try и/или ресурс остался открыт. 
Значение считать в ресурсе try, если при заведения животного аполнены все поля.
