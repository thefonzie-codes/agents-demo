import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ChatHistory from '../ChatHistory';

vi.mock('../api', () => ({
  getSessions: vi.fn(),
  deleteSession: vi.fn(),
  renameSession: vi.fn(),
}));

import { getSessions, deleteSession, renameSession } from '../api';

const mockSessions = [
  {
    session_id: 'session-1',
    title: 'First Conversation',
    created_at: '2024-01-01 10:00:00',
    updated_at: '2024-01-01 12:00:00',
  },
  {
    session_id: 'session-2',
    title: 'Second Conversation',
    created_at: '2024-01-02 10:00:00',
    updated_at: '2024-01-02 14:00:00',
  },
];

describe('ChatHistory', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    (getSessions as ReturnType<typeof vi.fn>).mockResolvedValue(mockSessions);
  });

  it('renders session list', async () => {
    render(
      <ChatHistory
        currentSessionId={null}
        onSelectSession={() => {}}
        onNewChat={() => {}}
        isOpen={true}
        onClose={() => {}}
      />
    );

    await waitFor(() => {
      expect(screen.getByText('First Conversation')).toBeInTheDocument();
      expect(screen.getByText('Second Conversation')).toBeInTheDocument();
    });
  });

  it('search filters sessions', async () => {
    render(
      <ChatHistory
        currentSessionId={null}
        onSelectSession={() => {}}
        onNewChat={() => {}}
        isOpen={true}
        onClose={() => {}}
      />
    );

    await waitFor(() => {
      expect(screen.getByText('First Conversation')).toBeInTheDocument();
    });

    const searchInput = screen.getByPlaceholderText('Search conversations...');
    fireEvent.change(searchInput, { target: { value: 'First' } });

    await waitFor(() => {
      expect(screen.getByText('First Conversation')).toBeInTheDocument();
      expect(screen.queryByText('Second Conversation')).not.toBeInTheDocument();
    });
  });

  it('calls onSelectSession when clicking a session', async () => {
    const onSelectSession = vi.fn();
    
    render(
      <ChatHistory
        currentSessionId={null}
        onSelectSession={onSelectSession}
        onNewChat={() => {}}
        isOpen={true}
        onClose={() => {}}
      />
    );

    await waitFor(() => {
      fireEvent.click(screen.getByText('First Conversation'));
    });

    expect(onSelectSession).toHaveBeenCalledWith('session-1');
  });

  it('calls onNewChat when clicking new chat button', async () => {
    const onNewChat = vi.fn();
    
    render(
      <ChatHistory
        currentSessionId={null}
        onSelectSession={() => {}}
        onNewChat={onNewChat}
        isOpen={true}
        onClose={() => {}}
      />
    );

    await waitFor(() => {
      fireEvent.click(screen.getByText('New chat'));
    });

    expect(onNewChat).toHaveBeenCalled();
  });

  it('shows empty state when no sessions', async () => {
    (getSessions as ReturnType<typeof vi.fn>).mockResolvedValue([]);
    
    render(
      <ChatHistory
        currentSessionId={null}
        onSelectSession={() => {}}
        onNewChat={() => {}}
        isOpen={true}
        onClose={() => {}}
      />
    );

    await waitFor(() => {
      expect(screen.getByText('No conversation history')).toBeInTheDocument();
    });
  });

  it('renders current session as active', async () => {
    render(
      <ChatHistory
        currentSessionId="session-1"
        onSelectSession={() => {}}
        onNewChat={() => {}}
        isOpen={true}
        onClose={() => {}}
      />
    );

    await waitFor(() => {
      expect(screen.getByText('First Conversation')).toBeInTheDocument();
    });
  });
});
