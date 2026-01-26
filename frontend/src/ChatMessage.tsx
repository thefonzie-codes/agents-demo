import Markdown from "react-markdown";
import type { Message } from "./types";

interface ChatMessageProps {
  message: Message;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-5`}>
      {/* Assistant avatar - Google-colored circle */}
      {!isUser && (
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-google-blue flex items-center justify-center mr-3 mt-0.5">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </div>
      )}

      <div
        className={`text-sm leading-relaxed ${
          isUser
            ? "max-w-[75%] bg-google-blue-light text-google-text rounded-2xl rounded-br-sm px-4 py-2.5 whitespace-pre-wrap"
            : "max-w-[85%] text-google-text markdown-body"
        }`}
      >
        {isUser ? message.text : <Markdown>{message.text}</Markdown>}
      </div>

      {/* User avatar */}
      {isUser && (
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-google-blue flex items-center justify-center text-white text-xs font-medium ml-3 mt-0.5">
          You
        </div>
      )}
    </div>
  );
}
