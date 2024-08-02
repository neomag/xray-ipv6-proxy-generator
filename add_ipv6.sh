#!/bin/bash

# Имя сетевого интерфейса
INTERFACE="eno0"

# Имя файла с IPv6 адресами
ADDRESS_FILE="NEWaddress.txt"

# Проверяем, существует ли файл
if [[ ! -f "$ADDRESS_FILE" ]]; then
    echo "Файл $ADDRESS_FILE не найден."
    exit 1
fi

# Читаем файл построчно и добавляем каждый адрес на интерфейс
while IFS= read -r address; do
    if [[ -n "$address" ]]; then  # Проверяем, что строка не пустая
        sudo ip -6 addr add "$address" dev "$INTERFACE" 2>&1 > /dev/null
        if [[ $? -ne 0 ]]; then
            echo "Ошибка при добавлении $address на $INTERFACE"
        fi
    fi
done < "$ADDRESS_FILE"
