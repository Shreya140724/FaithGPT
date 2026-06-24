"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";

export default function DailyVerse() {

  const [verse, setVerse] =
    useState<any>(null);

  useEffect(() => {

    api.get("/daily-verse")
      .then((res) =>
        setVerse(res.data)
      );

  }, []);

  if (!verse) return null;

  return (
    <div className="bg-gray-900 rounded-xl p-6 mb-8">

      <h2 className="text-2xl font-bold">
        ✝ Daily Verse
      </h2>

      <p className="mt-3">
        {verse.text}
      </p>

      <p className="text-blue-400 mt-3">
        {verse.reference}
      </p>

    </div>
  );
}