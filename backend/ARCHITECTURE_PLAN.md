# Multi-Agent Demo - Architecture Plan

## Overview

Building a multi-industry AI agent demonstration platform with:
- 5 industry-specific agents (Travel, Healthcare, Banking, E-commerce, Retail)
- Separate UI pages per industry
- Both CLI and web interfaces
- Ripple-based frontend
- Flask backend API
- Google Gemini 2.5 Flash for AI capabilities

## Architecture Principles

- **Reusable Agent Factory**: Single `Agent` class instantiated with industry-specific configs
- **Separate Databases**: Each industry has its own SQLite database with realistic mock data
- **RESTful API**: Flask backend exposes endpoints for each industry agent
- **Industry-Themed UI**: Each agent gets a dedicated page with custom branding/styling

---

## Phase 1: Foundation (Start Here)

**Goal**: Refactor existing travel agent to be reusable

### 1.1 Complete the Agent Factory Pattern

**Files**: `ai/agent.py`

- Fix the `Agent` class (currently has bugs - missing `self` parameters)
- Create a generic agent factory that can instantiate agents with:
  - Custom system instructions
  - Industry-specific database tools
  - Configurable models
  - Conversation history management
  - Tool calling capabilities

**Expected API**:
```python
agent = Agent(
    models=["gemini-2.5-flash"],
    tools=[query_db_declaration],
    system_instruction="You are a healthcare assistant..."
)
response = agent.call(prompt, chat_history)
```

### 1.2 Refactor Database Layer

**Create**: `db_manager.py` (base class)

- Create a base `DatabaseManager` class with methods:
  - `generate_db(path, schema_file, data_generator)`
  - `query_db(query)`
  - `delete_db(path)`
  - Safety checks (prevent DROP, etc.)

**Directory structure**:
```
sample_datasets/
  ├── travel_company_customer_db/
  │   ├── schema.sql
  │   ├── data.py
  │   ├── case_descriptions.py
  │   └── travel_company.db (generated)
  ├── healthcare_db/
  │   ├── schema.sql
  │   ├── data.py
  │   └── healthcare.db (generated)
  ├── banking_db/
  │   ├── schema.sql
  │   ├── data.py
  │   └── banking.db (generated)
  ├── ecommerce_db/
  │   ├── schema.sql
  │   ├── data.py
  │   └── ecommerce.db (generated)
  └── retail_db/
      ├── schema.sql
      ├── data.py
      └── retail.db (generated)
```

### 1.3 Create Industry Agent Configs

**Create**: `ai/configs/` directory

Each industry gets a config file:
- `ai/configs/travel_config.py`
- `ai/configs/healthcare_config.py`
- `ai/configs/banking_config.py`
- `ai/configs/ecommerce_config.py`
- `ai/configs/retail_config.py`

**Config structure**:
```python
SYSTEM_INSTRUCTION = """..."""
DB_PATH = "sample_datasets/healthcare_db/healthcare.db"
SCHEMA_PATH = "sample_datasets/healthcare_db/schema.sql"
TOOLS = [query_db_declaration]
```

### 1.4 Update CLI Interface

**Update**: `main.py`

- Add industry selection at startup
- Load appropriate config based on selection
- Instantiate agent using factory pattern
- Maintain conversation loop

---

## Phase 2: Web Backend (Flask API)

**Goal**: Create RESTful API for agents

### 2.1 Flask Application Structure

**File**: `flask_app.py` (new main Flask app)

```
flask_app.py          # Main Flask application
api/
  ├── __init__.py
  ├── routes/
  │   ├── __init__.py
  │   ├── travel.py
  │   ├── healthcare.py
  │   ├── banking.py
  │   ├── ecommerce.py
  │   └── retail.py
  └── session_manager.py  # Conversation history management
```

### 2.2 API Endpoints

**Chat Endpoints** (one per industry):
```
POST /api/chat/travel
POST /api/chat/healthcare
POST /api/chat/banking
POST /api/chat/ecommerce
POST /api/chat/retail
```

**Request body**:
```json
{
  "message": "What bookings does customer john@example.com have?",
  "session_id": "optional-uuid"
}
```

**Response**:
```json
{
  "response": "I found 2 bookings for john@example.com...",
  "session_id": "uuid",
  "tool_calls": [...],
  "timestamp": "2025-11-09T..."
}
```

**Additional Endpoints** (optional):
```
GET  /api/sessions/{session_id}           # Get chat history
DELETE /api/sessions/{session_id}         # Clear chat history
GET  /api/industries                      # List available industries
```

### 2.3 Session Management

**File**: `api/session_manager.py`

- Store conversation history in memory (or Redis for production)
- Automatic session expiry (e.g., 1 hour)
- Session ID generation
- Chat history serialization

---

## Phase 3: Frontend (Ripple)

**Goal**: Build separate pages per industry

### 3.1 Project Setup

```bash
npm create ripple@latest frontend
cd frontend
npm install
```

**Dependencies**:
- Ripple framework
- Axios (for API calls)
- React Router (for page navigation)
- TailwindCSS (for styling)

### 3.2 Page Structure

```
frontend/
  ├── src/
  │   ├── pages/
  │   │   ├── Home.jsx              # Landing page with industry cards
  │   │   ├── TravelAgent.jsx       # Travel industry chat
  │   │   ├── HealthcareAgent.jsx   # Healthcare chat
  │   │   ├── BankingAgent.jsx      # Banking chat
  │   │   ├── EcommerceAgent.jsx    # E-commerce chat
  │   │   └── RetailAgent.jsx       # Retail chat
  │   ├── components/
  │   │   ├── IndustryCard.jsx      # Card for industry selection
  │   │   ├── ChatInterface.jsx     # Reusable chat UI
  │   │   ├── MessageBubble.jsx     # Individual message component
  │   │   ├── IndustryLayout.jsx    # Wrapper with industry theming
  │   │   └── Header.jsx            # Navigation header
  │   ├── services/
  │   │   └── api.js                # API client for backend calls
  │   ├── utils/
  │   │   └── themes.js             # Industry color schemes
  │   └── App.jsx
  └── public/
```

### 3.3 Industry Theming

**File**: `src/utils/themes.js`

```javascript
export const themes = {
  travel: {
    primary: '#3B82F6',    // Blue
    secondary: '#60A5FA',
    gradient: 'from-blue-500 to-cyan-500'
  },
  healthcare: {
    primary: '#10B981',    // Green
    secondary: '#34D399',
    gradient: 'from-green-500 to-emerald-500'
  },
  banking: {
    primary: '#6366F1',    // Indigo
    secondary: '#818CF8',
    gradient: 'from-indigo-500 to-purple-500'
  },
  ecommerce: {
    primary: '#F59E0B',    // Amber
    secondary: '#FBBF24',
    gradient: 'from-amber-500 to-orange-500'
  },
  retail: {
    primary: '#EC4899',    // Pink
    secondary: '#F472B6',
    gradient: 'from-pink-500 to-rose-500'
  }
}
```

### 3.4 Component Architecture

**ChatInterface Component** (reusable):
- Message history display
- Input field with send button
- Loading states
- Error handling
- Auto-scroll to latest message

**IndustryLayout Component**:
- Takes industry prop
- Applies theme colors
- Shows industry-specific header/branding
- Wraps ChatInterface

---

## Phase 4: Database Schemas

### 4.1 Healthcare Database

**Tables**:
- `patients` - Patient demographics, medical history
- `appointments` - Scheduled appointments with doctors
- `doctors` - Doctor profiles and specializations
- `prescriptions` - Medication records
- `insurance_claims` - Insurance claim records
- `medical_records` - Visit notes and diagnoses

### 4.2 Banking Database

**Tables**:
- `customers` - Customer profiles
- `accounts` - Checking, savings, credit accounts
- `transactions` - Deposits, withdrawals, transfers
- `loans` - Loan applications and status
- `cards` - Credit/debit card information
- `support_tickets` - Customer service cases

### 4.3 E-commerce Database

**Tables**:
- `customers` - Customer profiles
- `products` - Product catalog
- `categories` - Product categories
- `orders` - Order records
- `order_items` - Line items per order
- `inventory` - Stock levels
- `reviews` - Product reviews
- `returns` - Return requests

### 4.4 Retail Database

**Tables**:
- `customers` - Loyalty program members
- `stores` - Store locations
- `products` - Product catalog
- `sales` - Point-of-sale transactions
- `inventory` - Stock per store location
- `employees` - Staff records
- `promotions` - Active promotions and discounts

---

## Phase 5: Polish & Features

### 5.1 Enhanced Features

- **Chat Export**: Download conversation as PDF/JSON
- **Chat History**: View past conversations
- **Agent Analytics**: Track most common queries
- **Multi-turn Context**: Maintain context across conversation
- **Suggested Queries**: Show example questions per industry
- **Database Insights**: Show sample data/statistics in UI

### 5.2 Error Handling

- Graceful API error responses
- Retry logic for failed requests
- User-friendly error messages
- Validation for malformed queries

### 5.3 Security

- Rate limiting on API endpoints
- Input sanitization
- SQL injection prevention (already in place with parameterized queries)
- CORS configuration
- Environment variable management

### 5.4 Performance

- Response caching for common queries
- Database connection pooling
- Frontend code splitting
- Lazy loading for chat history

---

## Development Workflow

### Recommended Order

1. **Fix Agent class** → Test with existing travel agent CLI
2. **Create one new industry** (e.g., healthcare) → Validate pattern works
3. **Set up Flask API** → Create endpoints for travel + healthcare
4. **Build basic Ripple frontend** → Test with 2 industries
5. **Add remaining industries** → Banking, e-commerce, retail
6. **Polish UI/UX** → Theming, error handling, features

### Testing Strategy

- **Unit tests**: `pytest` for database generation, agent logic
- **Integration tests**: API endpoint testing
- **E2E tests**: Frontend interaction testing
- **Manual testing**: Test each industry agent with realistic queries

---

## Technology Stack

### Backend
- **Python 3.x**
- **Flask** - Web framework
- **SQLite** - Database
- **Google Gemini API** - AI model
- **python-dotenv** - Environment management

### Frontend
- **Ripple** - Frontend framework
- **Axios** - HTTP client
- **TailwindCSS** - Styling
- **React Router** - Navigation

### DevOps
- **Nix** - Development environment
- **venv** - Python virtual environment
- **.env** - Configuration management

---

## File Structure (Final)

```
ai-agent-demo/
├── ai/
│   ├── __init__.py
│   ├── agent.py                    # Agent factory class
│   └── configs/
│       ├── travel_config.py
│       ├── healthcare_config.py
│       ├── banking_config.py
│       ├── ecommerce_config.py
│       └── retail_config.py
├── api/
│   ├── __init__.py
│   ├── session_manager.py
│   └── routes/
│       ├── __init__.py
│       ├── travel.py
│       ├── healthcare.py
│       ├── banking.py
│       ├── ecommerce.py
│       └── retail.py
├── sample_datasets/
│   ├── travel_company_customer_db/
│   ├── healthcare_db/
│   ├── banking_db/
│   ├── ecommerce_db/
│   └── retail_db/
├── frontend/                       # Ripple app
│   ├── src/
│   ├── public/
│   └── package.json
├── chat_logs/                      # CLI chat logs
├── __test__/
│   └── db_test.py
├── db_manager.py                   # Base database manager
├── db.py                          # Legacy (can refactor)
├── main.py                        # CLI interface
├── flask_app.py                   # Flask web server
├── requirements.txt
├── .env
├── CLAUDE.md
├── ARCHITECTURE_PLAN.md
└── README.md
```

---

## Notes

- Keep CLI interface for development/testing
- Web interface for demos and production
- Each industry is completely isolated (separate DB, config, routes)
- Agent factory makes adding new industries trivial
- Focus on getting MVP working, then iterate
