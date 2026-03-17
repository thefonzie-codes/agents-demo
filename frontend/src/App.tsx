import { useState, useRef, useEffect } from "react";
import { sendMessage, clearSession, getSession } from "./api";
import ChatMessage from "./ChatMessage";
import ChatHistory from "./ChatHistory";
import type { Message } from "./types";

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleSelectSession = async (selectedSessionId: string) => {
    try {
      const session = await getSession(selectedSessionId);
      setSessionId(session.session_id);
      setMessages(session.messages);
    } catch (err) {
      console.error("Failed to load session:", err);
    }
  };

  const handleNewChat = async () => {
    if (sessionId) {
      await clearSession(sessionId);
    }
    setMessages([]);
    setSessionId(null);
    inputRef.current?.focus();
  };

  const handleSend = async () => {
    const text = input.trim();
    if (!text || isLoading) return;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      text,
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const data = await sendMessage(text, sessionId);
      setSessionId(data.session_id);

      const assistantMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        text: data.response,
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      const errorMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        text: `Error: ${err instanceof Error ? err.message : "Something went wrong. Please try again."}`,
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex h-screen bg-google-surface font-sans">
      <ChatHistory
        currentSessionId={sessionId}
        onSelectSession={handleSelectSession}
        onNewChat={handleNewChat}
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      <div className="flex-1 flex flex-col min-w-0">
        <header className="bg-google-surface border-b border-google-border px-6 py-3 flex items-center gap-3 flex-shrink-0">
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="p-2 rounded-full hover:bg-google-hover"
          >
            <svg
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
            >
              <path d="M3 12h18M3 6h18M3 18h18" />
            </svg>
          </button>

          <div className="flex items-center gap-3">
            <div className="flex items-center gap-0.5">
              <span className="w-2.5 h-2.5 rounded-full bg-google-blue"></span>
              <span className="w-2.5 h-2.5 rounded-full bg-google-red"></span>
              <span className="w-2.5 h-2.5 rounded-full bg-google-yellow"></span>
              <span className="w-2.5 h-2.5 rounded-full bg-google-green"></span>
            </div>
            <h1 className="text-lg font-medium text-google-text">Travel Agent</h1>
            <span className="text-xs text-google-text-secondary bg-google-bg px-2 py-0.5 rounded-full">
              AI Assistant
            </span>
          </div>
        </header>

        <div className="flex-1 overflow-y-auto px-4 py-6 md:px-8 lg:px-16">
          {messages.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-full">
              <div className="flex items-center gap-1.5 mb-6">
                <span className="w-3.5 h-3.5 rounded-full bg-google-blue"></span>
                <span className="w-3.5 h-3.5 rounded-full bg-google-red"></span>
                <span className="w-3.5 h-3.5 rounded-full bg-google-yellow"></span>
                <span className="w-3.5 h-3.5 rounded-full bg-google-green"></span>
              </div>
              <h2 className="text-2xl font-normal text-google-text mb-2">
                Hello, how can I help?
              </h2>
              <p className="text-sm text-google-text-secondary text-center max-w-lg mb-8">
                I'm your travel company assistant. Ask me about customers,
                bookings, destinations, packages, payments, or support cases.
              </p>
              <div className="flex flex-wrap gap-2 justify-center max-w-xl">
                {[
                  "How many customers do we have?",
                  "Show me high-priority open cases",
                  "Find bookings for this month",
                ].map((suggestion) => (
                  <button
                    key={suggestion}
                    onClick={() => {
                      setInput(suggestion);
                      inputRef.current?.focus();
                    }}
                    className="px-4 py-2.5 bg-google-surface border border-google-border rounded-full text-sm text-google-text-secondary hover:bg-google-hover transition-colors cursor-pointer"
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="max-w-3xl mx-auto">
              {messages.map((msg) => (
                <ChatMessage key={msg.id} message={msg} />
              ))}
              {isLoading && (
                <div className="flex justify-start mb-5">
                  <div className="flex-shrink-0 w-8 h-8 rounded-full bg-google-blue flex items-center justify-center mr-3 mt-0.5">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  </div>
                  <div className="flex gap-1.5 items-center pt-2">
                    <span className="w-2 h-2 rounded-full bg-google-blue google-dot" style={{ animationDelay: "0s" }}></span>
                    <span className="w-2 h-2 rounded-full bg-google-red google-dot" style={{ animationDelay: "0.2s" }}></span>
                    <span className="w-2 h-2 rounded-full bg-google-yellow google-dot" style={{ animationDelay: "0.4s" }}></span>
                    <span className="w-2 h-2 rounded-full bg-google-green google-dot" style={{ animationDelay: "0.6s" }}></span>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        <div className="px-4 pb-6 pt-2 md:px-8 lg:px-16 flex-shrink-0">
          <div className="max-w-3xl mx-auto relative">
            <div className="flex items-center border border-google-border rounded-full bg-google-surface shadow-[0_1px_3px_0_rgba(60,64,67,0.15)] hover:shadow-[0_1px_3px_1px_rgba(60,64,67,0.2)] transition-shadow focus-within:shadow-[0_1px_3px_1px_rgba(60,64,67,0.2)]">
              <textarea
                ref={inputRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask about customers, bookings, cases..."
                rows={1}
                className="flex-1 resize-none bg-transparent px-5 py-3.5 text-sm text-google-text placeholder:text-google-text-secondary focus:outline-none"
              />
              <button
                onClick={handleSend}
                disabled={!input.trim() || isLoading}
                className="flex-shrink-0 w-10 h-10 mr-1.5 rounded-full flex items-center justify-center bg-google-blue text-white disabled:bg-google-hover disabled:text-google-text-secondary transition-colors cursor-pointer disabled:cursor-not-allowed"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
