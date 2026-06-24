"use client";

import { useState } from "react";
import api from "@/lib/api";

export default function PrayerAssistant() {

  const [problem, setProblem] =
    useState("");

  const [prayer, setPrayer] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const generatePrayer =
    async () => {

      if (!problem.trim())
        return;

      try {

        setLoading(true);

        const response =
          await api.post(
            "/prayer",
            {
              problem,
            }
          );

        setPrayer(
          response.data.prayer
        );

      } catch (error) {

        console.error(error);

        setPrayer(
          "Failed to generate prayer."
        );

      } finally {

        setLoading(false);

      }
    };

  return (

    <div
      className="
        bg-gray-900
        rounded-2xl
        p-6
        mt-10
      "
    >

      <h2
        className="
          text-3xl
          font-bold
          mb-4
        "
      >
        🙏 Prayer Assistant
      </h2>

      <textarea
        rows={4}
        value={problem}
        onChange={(e) =>
          setProblem(
            e.target.value
          )
        }
        placeholder="
Tell me what you need prayer for...
        "
        className="
          w-full
          bg-black
          border
          border-gray-700
          rounded-xl
          p-4
          text-white
        "
      />

      <button
        onClick={
          generatePrayer
        }
        disabled={
          loading
        }
        className="
          mt-4
          bg-green-600
          hover:bg-green-700
          px-6
          py-3
          rounded-lg
          font-semibold
        "
      >
        {loading
          ? "Generating..."
          : "Generate Prayer"}
      </button>

      {prayer && (

        <div
          className="
            mt-6
            bg-black
            border
            border-gray-700
            rounded-xl
            p-5
          "
        >

          <div
            className="
              whitespace-pre-wrap
              leading-8
            "
          >
            {prayer}
          </div>

        </div>

      )}

    </div>

  );
}