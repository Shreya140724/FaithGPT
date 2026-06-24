"use client";

import { useState } from "react";
import api from "@/lib/api";

export default function ImageGenerator() {
  const [prompt, setPrompt] = useState("");
  const [imagePath, setImagePath] = useState("");
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/generate-image",
        {
          prompt,
        }
      );

      setImagePath(
        response.data.image_path
      );
    } catch (error) {
      console.error(error);
      alert("Image generation failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-gray-900 p-6 rounded-xl">

      <h2 className="text-3xl font-bold mb-4">
        Image Generation
      </h2>

      <textarea
        rows={4}
        value={prompt}
        onChange={(e) =>
          setPrompt(e.target.value)
        }
        placeholder="Describe image..."
        className="
        w-full
        p-4
        rounded
        bg-black
        text-white
        border
        border-gray-700
        "
      />

      <button
        onClick={generateImage}
        className="
        mt-4
        bg-green-600
        px-5
        py-3
        rounded
        "
      >
        {loading
          ? "Generating..."
          : "Generate Image"}
      </button>

      {imagePath && (
        <div className="mt-6">

          <p className="mb-2">
            Generated Image
          </p>

          <img
            src={`http://127.0.0.1:8000/${imagePath}`}
            alt="Generated"
            className="
            rounded-xl
            border
            border-gray-700
            "
          />
        </div>
      )}
    </div>
  );
}