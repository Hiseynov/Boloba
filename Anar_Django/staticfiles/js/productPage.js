const apiUrl = 'http://127.0.0.1:8000/az/api/shops/';

async function fetchProducts() {
    try {
        const response = await fetch(apiUrl);
        console.log(response.body);
        
        // Проверка успешности ответа
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Разбор JSON-ответа
        const data = await response.json();

        // Проверка наличия results и его тип
        if (Array.isArray(data.results)) {
            console.log(data.results); // Данные успешно получены и выведены в консоль
            return data.results;
        } else {
            throw new Error('Expected data.results to be an array');
        }
    } catch (error) {
        console.error('Error fetching products:', error);
        return []; // Возвращаем пустой массив в случае ошибки
    }
}

// Вызов функции
fetchProducts()
