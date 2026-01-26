CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    country TEXT,
    date_of_birth DATE,
    passport_number TEXT,
    preferred_language TEXT,
    loyalty_points INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE destinations (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,           -- e.g., "Paris, France"
    country TEXT NOT NULL,
    description TEXT,
    popular_season TEXT,          -- e.g., "Summer", "Year-round"
    avg_price_per_day REAL
);

CREATE TABLE packages (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,           -- e.g., "Weekend in Paris"
    destination_id INTEGER,
    duration_days INTEGER,
    price REAL,
    description TEXT,
    category TEXT,                -- e.g., "Adventure", "Luxury", "Budget"
    max_capacity INTEGER,
    current_bookings INTEGER DEFAULT 0,
    FOREIGN KEY (destination_id) REFERENCES destinations(id)
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    package_id INTEGER,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    travel_start_date DATE,
    travel_end_date DATE,
    number_of_travelers INTEGER,
    total_price REAL,
    status TEXT,                 -- "Confirmed", "Pending", "Cancelled"
    special_requests TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (package_id) REFERENCES packages(id)
);

CREATE TABLE payments (
    id INTEGER PRIMARY KEY,
    booking_id INTEGER,
    amount REAL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT,        -- "Credit Card", "PayPal", "Bank Transfer"
    transaction_id TEXT,
    status TEXT,                -- "Completed", "Pending", "Failed"
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);

CREATE TABLE cases (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    booking_id INTEGER,         -- Optional: link to specific booking if relevant
    case_type TEXT NOT NULL,    -- "customer_support", "billing", "technical_support", etc.
    subject TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'Open', -- "Open", "In Progress", "Resolved", "Closed"
    priority TEXT DEFAULT 'Medium', -- "Low", "Medium", "High", "Critical"
    assigned_to TEXT,           -- Support agent name
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);