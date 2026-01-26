const API_BASE = "http://localhost:5000";

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
