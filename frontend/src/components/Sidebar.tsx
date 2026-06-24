"use client";

import HistorySidebar from "./HistorySidebar";

export default function Sidebar({
  onSelectChat,
}: {
  onSelectChat: (chat: any) => void;
}) {
  return (
    <div
      className="
        w-72
        h-screen
        overflow-y-auto
        bg-gray-950
        border-r
        border-gray-800
        p-6
      "
    >
      <h1
        className="
          text-3xl
          font-bold
          mb-8
        "
      >
        ✝ FaithGPT
      </h1>

      <button
        onClick={() => window.location.reload()}
        className="
          w-full
          bg-blue-600
          hover:bg-blue-700
          rounded-lg
          py-3
          font-semibold
          mb-6
          transition
        "
      >
        + New Chat
      </button>

      <hr className="border-gray-800 mb-6" />

      <HistorySidebar
        onSelectChat={onSelectChat}
      />
    </div>
  );
}