import React, { useState, useEffect } from "react";
import { getTodos, createTodo, removeTodo } from "./utils";
import "./App.css";

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState([]);

  useEffect(() => {
    getTodos(setTodos);
  }, []);

  const handleInputChange = (e) => {
    setNewTodo(e.target.value);
  };

  const handleAddTodo = () => {
    createTodo(newTodo, setNewTodo, setTodos);
  };

  const handleDeleteTodo = (id) => {
    removeTodo(id, setTodos);
  };

  return (
    <div className="App">
      <h1>Todo Application</h1>
      <div>
        <input
          type="text"
          placeholder="Add a new task"
          value={newTodo}
          onChange={handleAddTodo}
        />
        <button onClick={handleAddTodo}>Add Todo</button>
      </div>
      <div>
        <h3>Todos</h3>
        <ul>
          {todos.map((todo) => (
            <li key={todo.id}>
              {todo.item}
              <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
