const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:5000";

export interface Message {
  id: string;
  role: "user" | "assistant";
  text: string;
}

export interface ChatSession {
  session_id: string;
  title: string;
  messages: Message[];
  created_at: string;
  updated_at: string;
}

export interface ChatSessionMeta {
  session_id: string;
  title: string;
  created_at: string;
  updated_at: string;
}

export interface ChatResponse {
  response: string;
  session_id: string;
}

export interface ChatError {
  error: string;
}

export async function sendMessage(
  message: string,
  sessionId: string | null
): Promise<ChatResponse> {
  const body: Record<string, string> = { message };
  if (sessionId) {
    body.session_id = sessionId;
  }

  const res = await fetch(`${API_BASE}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const err: ChatError = await res.json();
    throw new Error(err.error || "Request failed");
  }

  return res.json();
}

export async function clearSession(sessionId: string): Promise<void> {
  await fetch(`${API_BASE}/api/session/${sessionId}`, {
    method: "DELETE",
  });
}

export async function getSessions(): Promise<ChatSessionMeta[]> {
  const res = await fetch(`${API_BASE}/api/sessions`);
  if (!res.ok) {
    throw new Error("Failed to fetch sessions");
  }
  const data = await res.json();
  return data.sessions;
}

export async function getSession(sessionId: string): Promise<ChatSession> {
  const res = await fetch(`${API_BASE}/api/sessions/${sessionId}`);
  if (!res.ok) {
    throw new Error("Session not found");
  }
  return res.json();
}

export async function deleteSession(sessionId: string): Promise<void> {
  const res = await fetch(`${API_BASE}/api/sessions/${sessionId}`, {
    method: "DELETE",
  });
  if (!res.ok) {
    throw new Error("Failed to delete session");
  }
}

export async function renameSession(
  sessionId: string,
  title: string
): Promise<void> {
  const res = await fetch(`${API_BASE}/api/sessions/${sessionId}/rename`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  if (!res.ok) {
    throw new Error("Failed to rename session");
  }
}
