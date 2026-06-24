"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";

export default function HistorySidebar() {

  const [history, setHistory] = useState<any[]>([]);

  const loadHistory = async () => {

    try {

      const res = await api.get(
        "/history/1"
      );

      setHistory(
        res.data
      );

    } catch (err) {

      console.error(err);

    }
  };

  useEffect(() => {

    loadHistory();

    window.addEventListener(
      "historyUpdated",
      loadHistory
    );

    return () => {

      window.removeEventListener(
        "historyUpdated",
        loadHistory
      );

    };

  }, []);

  const deleteChat = async (
    chatId: number
  ) => {

    try {

      await api.delete(
        `/history/${chatId}`
      );

      loadHistory();

    } catch (err) {

      console.error(err);

    }

  };

  return (

    <div>

      <h2
        className="
          text-2xl
          font-bold
          mb-4
        "
      >
        Chat History
      </h2>

      <div className="space-y-3">

        {history.map((chat) => (

          <div
            key={chat.id}
            className="
              bg-gray-800
              rounded-lg
              p-3
            "
          >

            <div
              className="
                text-sm
                font-medium
                truncate
              "
            >
              {chat.question}
            </div>

            <div
              className="
                flex
                justify-end
                mt-2
              "
            >

              <button
                onClick={() =>
                  deleteChat(chat.id)
                }
                className="
                  text-red-400
                  hover:text-red-300
                  text-xs
                "
              >
                🗑 Delete
              </button>

            </div>

          </div>

        ))}

      </div>

    </div>

  );
}