#!/bin/bash
# Функция, формирующая отчет
function report_creation {
echo 'Отчет о логе веб-сервера'
echo '========================'
echo "Общее количество запросов: `awk 'END {print NR}' access.log`"
echo "Количество уникальных IP-адресов: `awk '{ip[$1]++} END {for (i in ip) ++c} END {print c}' access.log`"
echo 'Количество запросов по методам:'
awk '/GET/ {++c} END {if (c > 0) print "  ", c, "GET"}' access.log
awk '/POST/ {++c} END {if (c > 0) print "  ", c, "POST"}' access.log
awk '/PUT/ {++c} END {if (c > 0) print "  ", c, "PUT"}' access.log
awk '/DELETE/ {++c} END {if (c > 0) print "  ", c, "DELETE"}' access.log
echo "Самый популярный URL: `awk '{url[$7]++} END {for (i in url) if (url[i] > max) {max = url[i]; maxurl = i}} END {print max, maxurl}' access.log`"
}
# Имя файла с отчетом
file_name='report.txt'
echo "Отчет сохранен в файл $file_name"
# Вывод результатов работы функции в файл
report_creation > $file_name
