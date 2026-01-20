const API_BASE = 'http://localhost:8000'; // Assuming backend runs on 8000

const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

async function loadTodos() {
    const response = await fetch(`${API_BASE}/todos`);
    const todos = await response.json();
    renderTodos(todos);
}

function renderTodos(todos) {
    todoList.innerHTML = '';
    todos.forEach(todo => {
        const li = document.createElement('li');
        li.className = 'list-group-item d-flex justify-content-between align-items-center';
        li.innerHTML = `
            <div>
                <input type="checkbox" ${todo.completed ? 'checked' : ''} onchange="toggleTodo(${todo.id}, this.checked)">
                <span class="${todo.completed ? 'text-decoration-line-through' : ''}">${todo.title}</span>
            </div>
            <button class="btn btn-danger btn-sm" onclick="deleteTodo(${todo.id})">Delete</button>
        `;
        todoList.appendChild(li);
    });
}

async function addTodo() {
    const title = todoInput.value.trim();
    if (!title) return;
    await fetch(`${API_BASE}/todos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });
    todoInput.value = '';
    loadTodos();
}

async function toggleTodo(id, completed) {
    await fetch(`${API_BASE}/todos/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed })
    });
    loadTodos();
}

async function deleteTodo(id) {
    await fetch(`${API_BASE}/todos/${id}`, {
        method: 'DELETE'
    });
    loadTodos();
}

addBtn.addEventListener('click', addTodo);
todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTodo();
});

loadTodos();