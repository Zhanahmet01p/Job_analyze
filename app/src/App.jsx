import { useState } from "react";
import "./index.scss";
import Job from "./components/job";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Job />
    </>
  );
}

export default App;
