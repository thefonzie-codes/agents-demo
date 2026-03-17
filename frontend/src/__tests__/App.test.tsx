import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from '../App';

vi.mock('../api', () => ({
  sendMessage: vi.fn(),
  clearSession: vi.fn(),
  getSession: vi.fn(),
  getSessions: vi.fn().mockResolvedValue([]),
}));

import { sendMessage, clearSession, getSession, getSessions } from '../api';

describe('App', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    (getSessions as ReturnType<typeof vi.fn>).mockResolvedValue([]);
  });

  it('renders empty state', () => {
    render(<App />);
    
    expect(screen.getByText('Hello, how can I help?')).toBeInTheDocument();
  });

  it('renders suggestion buttons', () => {
    render(<App />);
    
    expect(screen.getByText('How many customers do we have?')).toBeInTheDocument();
    expect(screen.getByText('Show me high-priority open cases')).toBeInTheDocument();
    expect(screen.getByText('Find bookings for this month')).toBeInTheDocument();
  });

  it('fills input when suggestion is clicked', () => {
    render(<App />);
    
    const suggestionButton = screen.getByText('How many customers do we have?');
    fireEvent.click(suggestionButton);
    
    const input = screen.getByPlaceholderText('Ask about customers, bookings, cases...');
    expect(input).toHaveValue('How many customers do we have?');
  });

  it('sends message when send button is clicked', async () => {
    (sendMessage as ReturnType<typeof vi.fn>).mockResolvedValue({
      response: 'We have 10,000 customers.',
      session_id: 'new-session-id',
    });
    
    render(<App />);
    
    const input = screen.getByPlaceholderText('Ask about customers, bookings, cases...');
    fireEvent.change(input, { target: { value: 'How many customers?' } });
    
    const buttons = screen.getAllByRole('button');
    const sendButton = buttons.find(b => b.querySelector('path[d="M5 12h14M12 5l7 7-7 7"]'));
    fireEvent.click(sendButton!);
    
    await waitFor(() => {
      expect(sendMessage).toHaveBeenCalledWith('How many customers?', null);
    });
  });

  it('does not send empty message', () => {
    render(<App />);
    
    const buttons = screen.getAllByRole('button');
    const sendButton = buttons.find(b => b.querySelector('path[d="M5 12h14M12 5l7 7-7 7"]'));
    fireEvent.click(sendButton!);
    
    expect(sendMessage).not.toHaveBeenCalled();
  });

  it('shows error message on failure', async () => {
    (sendMessage as ReturnType<typeof vi.fn>).mockRejectedValue(new Error('Network error'));
    
    render(<App />);
    
    const input = screen.getByPlaceholderText('Ask about customers, bookings, cases...');
    fireEvent.change(input, { target: { value: 'Test message' } });
    
    const buttons = screen.getAllByRole('button');
    const sendButton = buttons.find(b => b.querySelector('path[d="M5 12h14M12 5l7 7-7 7"]'));
    fireEvent.click(sendButton!);
    
    await waitFor(() => {
      expect(screen.getByText(/Error:/)).toBeInTheDocument();
    });
  });
});
