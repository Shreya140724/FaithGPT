"use client";

import { useState } from "react";

import api from "@/lib/api";

import Sidebar from "@/components/Sidebar";
import DailyVerse from "@/components/DailyVerse";
import ImageGenerator from "@/components/ImageGenerator";
import PrayerAssistant from "@/components/PrayerAssistant";


export default function Home() {
  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const [citations, setCitations] =
    useState<string[]>([]);

  const [loading, setLoading] =
    useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const response =
        await api.post("/chat", {
          user_id: 1,
          question,
        });

      setAnswer(
        response.data.answer
      );

      setCitations(
        response.data.citations || []
      );

      window.dispatchEvent(
        new Event("historyUpdated")
      );
    } catch (error) {
      console.error(error);

      setAnswer(
        "Failed to connect to backend."
      );

      setCitations([]);
    } finally {
      setLoading(false);
    }
  };

  const loadChat = (
    chat: any
  ) => {
    setQuestion(chat.question);

    setAnswer(chat.answer);
  };

  return (
    <div className="flex min-h-screen bg-black text-white">

      <Sidebar
        onSelectChat={loadChat}
      />

      <main className="flex-1 p-10 overflow-y-auto">

        <DailyVerse />

        <div
          className="
            bg-gray-900
            rounded-2xl
            p-6
            mt-8
          "
        >
          <h2
            className="
              text-3xl
              font-bold
              mb-6
            "
          >
            Bible Chat
          </h2>

          <textarea
            rows={5}
            value={question}
            onChange={(e) =>
              setQuestion(
                e.target.value
              )
            }
            placeholder="Ask a Bible question..."
            className="
              w-full
              rounded-xl
              bg-black
              text-white
              border
              border-gray-700
              p-4
              text-lg
              focus:outline-none
            "
          />

          <button
            onClick={askQuestion}
            disabled={loading}
            className="
              mt-4
              bg-blue-600
              hover:bg-blue-700
              px-6
              py-3
              rounded-lg
              font-semibold
            "
          >
            {loading
              ? "Thinking..."
              : "Ask FaithGPT"}
          </button>

          {answer && (
            <div className="mt-8">

              <h3
                className="
                  text-2xl
                  font-bold
                  mb-4
                "
              >
                Answer
              </h3>

              <div
                className="
                  bg-black
                  border
                  border-gray-700
                  rounded-xl
                  p-6
                "
              >
                <p
                  className="
                    whitespace-pre-wrap
                    leading-8
                  "
                >
                  {answer}
                </p>
              </div>

              {citations.length >
                0 && (
                <>
                  <h3
                    className="
                      text-xl
                      font-semibold
                      mt-6
                      mb-3
                    "
                  >
                    References
                  </h3>

                  <ul className="space-y-2">
                    {citations.map(
                      (
                        citation
                      ) => (
                        <li
                          key={
                            citation
                          }
                          className="
                            text-blue-400
                          "
                        >
                          •{" "}
                          {
                            citation
                          }
                        </li>
                      )
                    )}
                  </ul>
                </>
              )}
            </div>
          )}
        </div>

        <div className="mt-10">
          <ImageGenerator />
        </div>

        <div className="mt-10">
          <PrayerAssistant />
        </div>

      </main>
    </div>
  );
}