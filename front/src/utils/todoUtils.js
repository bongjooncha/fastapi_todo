import { addTodo, fetchTodos, deleteTodo } from "../api";

export async function getTodos(setTodos) {
  try {
    const todos = await fetchTodos();
    setTodos(todos);
  } catch (error) {
    console.error("Todo 목록을 불러오는데 실패.");
  }
}

export async function createTodo(newTodo, setNewTodo, setTodos) {
  if (newTodo.trim() !== "") {
    try {
      await addTodo(newTodo);
      setNewTodo("");
      getTodos(setTodos);
    } catch (error) {
      console.log("Todo 추가에 실패: ", error);
    }
  }
}

export async function removeTodo(id, setTodos) {
  try {
    await deleteTodo(id);
    getTodos(setTodos);
  } catch (error) {
    console.error("Todo 삭제에 실패했습니다:", error);
  }
}
