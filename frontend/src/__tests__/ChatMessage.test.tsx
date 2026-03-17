import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import ChatMessage from '../ChatMessage';

describe('ChatMessage', () => {
  it('renders user message correctly', () => {
    const message = {
      id: '1',
      role: 'user' as const,
      text: 'Hello, world!',
    };

    render(<ChatMessage message={message} />);
    
    expect(screen.getByText('Hello, world!')).toBeInTheDocument();
  });

  it('renders assistant message', () => {
    const message = {
      id: '2',
      role: 'assistant' as const,
      text: 'This is a response',
    };

    render(<ChatMessage message={message} />);
    
    expect(screen.getByText('This is a response')).toBeInTheDocument();
  });

  it('renders markdown tables', () => {
    const message = {
      id: '3',
      role: 'assistant' as const,
      text: `| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |`,
    };

    render(<ChatMessage message={message} />);
    
    expect(screen.getByText('Header 1')).toBeInTheDocument();
    expect(screen.getByText('Cell 1')).toBeInTheDocument();
  });

  it('renders code blocks', () => {
    const message = {
      id: '4',
      role: 'assistant' as const,
      text: 'Here is some code:\n```js\nconst x = 1;\n```',
    };

    render(<ChatMessage message={message} />);
    
    expect(screen.getByText('const x = 1;')).toBeInTheDocument();
  });
});
