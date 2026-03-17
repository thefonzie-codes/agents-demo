import { useState } from "react";
import { getSessions, deleteSession, renameSession, type ChatSessionMeta } from "./api";

interface ChatHistoryProps {
  currentSessionId: string | null;
  onSelectSession: (sessionId: string) => void;
  onNewChat: () => void;
  isOpen: boolean;
  onClose: () => void;
}

export default function ChatHistory({
  currentSessionId,
  onSelectSession,
  onNewChat,
  isOpen,
  onClose,
}: ChatHistoryProps) {
  const [sessions, setSessions] = useState<ChatSessionMeta[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editingTitle, setEditingTitle] = useState("");
  const [initialLoadDone, setInitialLoadDone] = useState(false);

  const loadSessions = async () => {
    try {
      const data = await getSessions();
      setSessions(data);
    } catch (err) {
      console.error("Failed to load sessions:", err);
    }
  };

  if (isOpen && !initialLoadDone) {
    loadSessions();
    setInitialLoadDone(true);
  }

  const handleDelete = async (
    e: React.MouseEvent,
    sessionId: string
  ) => {
    e.stopPropagation();
    try {
      await deleteSession(sessionId);
      await loadSessions();
      if (currentSessionId === sessionId) {
        onNewChat();
      }
    } catch (err) {
      console.error("Failed to delete session:", err);
    }
  };

  const handleRename = async (sessionId: string) => {
    if (!editingTitle.trim()) {
      setEditingId(null);
      return;
    }
    try {
      await renameSession(sessionId, editingTitle.trim());
      setEditingId(null);
      await loadSessions();
    } catch (err) {
      console.error("Failed to rename session:", err);
    }
  };

  const startEditing = (e: React.MouseEvent, session: ChatSessionMeta) => {
    e.stopPropagation();
    setEditingId(session.session_id);
    setEditingTitle(session.title);
  };

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

    if (diffDays === 0) {
      return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    } else if (diffDays === 1) {
      return "Yesterday";
    } else if (diffDays < 7) {
      return date.toLocaleDateString([], { weekday: "short" });
    } else {
      return date.toLocaleDateString([], { month: "short", day: "numeric" });
    }
  };

  const filteredSessions = sessions.filter((s) =>
    s.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  if (!isOpen) return null;

  return (
    <div className="w-72 bg-google-surface border-r border-google-border flex flex-col h-full">
      <div className="p-4 border-b border-google-border flex items-center justify-between">
        <span className="text-sm font-medium text-google-text">History</span>
        <button
          onClick={onClose}
          className="p-1.5 rounded-full hover:bg-google-hover"
        >
          <svg
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
          >
            <path d="M18 6L6 18M6 6l12 12" />
          </svg>
        </button>
      </div>

      <div className="p-4 border-b border-google-border">
        <button
          onClick={onNewChat}
          className="w-full flex items-center justify-center gap-2 px-4 py-2.5 bg-google-blue text-white text-sm font-medium rounded-full hover:bg-google-blue/90 transition-colors"
        >
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M12 5v14M5 12h14" />
          </svg>
          New chat
        </button>
      </div>

      <div className="p-3">
        <input
          type="text"
          placeholder="Search conversations..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full px-3 py-2 text-sm bg-google-bg border border-google-border rounded-lg focus:outline-none focus:border-google-blue placeholder:text-google-text-secondary"
        />
      </div>

      <div className="flex-1 overflow-y-auto">
        {filteredSessions.length === 0 ? (
          <div className="p-4 text-center text-sm text-google-text-secondary">
            {searchQuery ? "No matching conversations" : "No conversation history"}
          </div>
        ) : (
          <div className="p-2">
            {filteredSessions.map((session) => (
              <div
                key={session.session_id}
                onClick={() => onSelectSession(session.session_id)}
                className={`group flex items-center justify-between p-3 rounded-lg cursor-pointer mb-1 ${
                  currentSessionId === session.session_id
                    ? "bg-google-blue-light"
                    : "hover:bg-google-hover"
                }`}
              >
                <div className="flex-1 min-w-0 mr-2">
                  {editingId === session.session_id ? (
                    <input
                      type="text"
                      value={editingTitle}
                      onChange={(e) => setEditingTitle(e.target.value)}
                      onBlur={() => handleRename(session.session_id)}
                      onKeyDown={(e) => {
                        if (e.key === "Enter") handleRename(session.session_id);
                        if (e.key === "Escape") setEditingId(null);
                      }}
                      onClick={(e) => e.stopPropagation()}
                      autoFocus
                      className="w-full px-2 py-1 text-sm bg-white border border-google-blue rounded focus:outline-none"
                    />
                  ) : (
                    <div className="text-sm text-google-text truncate">
                      {session.title}
                    </div>
                  )}
                  <div className="text-xs text-google-text-secondary mt-0.5">
                    {formatDate(session.updated_at)}
                  </div>
                </div>
                <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                  <button
                    onClick={(e) => startEditing(e, session)}
                    className="p-1.5 rounded hover:bg-google-border"
                    title="Rename"
                  >
                    <svg
                      width="14"
                      height="14"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                    >
                      <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" />
                      <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" />
                    </svg>
                  </button>
                  <button
                    onClick={(e) => handleDelete(e, session.session_id)}
                    className="p-1.5 rounded hover:bg-google-border text-red-500"
                    title="Delete"
                  >
                    <svg
                      width="14"
                      height="14"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                    >
                      <path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
                    </svg>
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
