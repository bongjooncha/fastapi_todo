import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/todo";

export async function fetchTodos() {
  const response = await axios.get(API_BASE_URL);
  return response.data.todos;
}

export async function addTodo(item) {
  await axios.post(API_BASE_URL, { item });
}

export async function deleteTodo(id) {
  await axios.delete(`${API_BASE_URL}/${id}`);
}
