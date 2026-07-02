import { useState } from "react";

interface LearningItem {
  text: string;
}

export default function LearningTracker() {
  const [items, setItems] = useState<LearningItem[]>([]);
  const [draft, setDraft] = useState("");

  function addItem() {
    if (draft.trim() === "") return;
    setItems([...items, { text: draft }]);
    setDraft("");
  }

  function deleteItem(index: number) {
    setItems(items.filter((_, i) => i !== index));
  }

  return (
    <div>
      <h2>Things I'm Learning</h2>
        <input value={draft} onChange={(e) => setDraft(e.target.value)} />
        <button onClick={addItem}>Add</button>
      <ul>
        {items.map((item, i) => (
          <li key={i}>
            {item.text} <button onClick={() => deleteItem(i)}>×</button>
          </li>
        ))}
      </ul>
    </div>
  );
}