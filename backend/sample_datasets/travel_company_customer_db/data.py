"""Data lists for generating travel company customer database data."""

FIRST_NAMES = {
    # Western/Anglo names
    "Ethan", "Olivia", "Liam", "Emma", "Noah", "Ava", "William", "Sophia",
    "James", "Isabella", "Benjamin", "Charlotte", "Lucas", "Amelia", "Henry",
    "Mia", "Alexander", "Evelyn", "Theodore", "Harper", "Jackson", "Victoria",
    "Sebastian", "Grace", "Michael", "Daniel", "Chloe", "Matthew", "Penelope",
    "David", "Zoe", "Joseph", "Layla", "Andrew", "Aria", "Samuel", "Riley",
    "Joshua", "Ryan", "Nicholas", "Natalie", "Kevin", "Hannah", "Connor",
    "Audrey", "Justin", "Avery", "Brayden", "Eleanor", "Aaron", "Maya",
    "Tyler", "Stella", "Cameron", "Savannah", "Christian", "Violet", "Hunter",
    "Aubrey", "Elijah", "Scarlett", "Adrian", "Madelyn", "Jason", "Skylar",
    "Brandon", "Paisley", "Jaxon", "Nora", "Adam", "Ezra", "Thomas", "Lily",
    "Logan", "Dylan", "Jack", "Emily", "Oliver", "Sophia", "Mason", "Ava",
    
    # Spanish/Latin American names
    "Diego", "Sofia", "Carlos", "Isabella", "Miguel", "Valentina", "Javier",
    "Camila", "Andres", "Ana", "Ricardo", "Lucia", "Fernando", "Elena",
    "Alejandro", "María", "Gabriel", "Sara", "Mateo", "Andrea", "Rafael",
    "Natalia", "Luis", "Carmen", "Pedro", "Isabel", "Juan", "Rosa",
    "Santiago", "Ana Sofia", "Daniel", "Paula", "Jose", "Laura", "Francisco",
    
    # Asian names - Chinese
    "Wei", "Mei", "Jun", "Ling", "Zhang", "Jing", "Li", "Xia", "Chen", "Yan",
    "Hui", "Min", "Feng", "Yu", "Xin", "Fang", "Yong", "Lin", "Bin", "Qi",
    
    # Asian names - Japanese
    "Hiroshi", "Yuki", "Takeshi", "Aiko", "Kenji", "Emiko", "Ryota", "Mika",
    "Daiki", "Sakura", "Kenta", "Akiko", "Yuki", "Naomi", "Shota", "Yuki",
    "Taro", "Haru", "Satoshi", "Midori",
    
    # Asian names - Korean
    "Jin", "Soo", "Min", "Ji", "Hoon", "Yeon", "Seung", "Hye", "Tae", "Eun",
    "Jae", "Mi", "Sang", "Joo", "Woo", "Hyun", "Kyung", "Young",
    
    # Asian names - Indian
    "Priya", "Arjun", "Anjali", "Rohan", "Sneha", "Vikram", "Deepa", "Raj",
    "Neha", "Amit", "Riya", "Karan", "Meera", "Aryan", "Radha", "Krishna",
    "Geeta", "Sunil", "Preeti", "Nikhil",
    
    # Asian names - Filipino/Southeast Asian
    "Maria", "Juan", "Ana", "Carlos", "Rosario", "Francisco", "Carmen",
    "Miguel", "Rosa", "Jose", "Angel", "Ramon", "Angelina", "Fernando",
    
    # Middle Eastern names
    "Ahmed", "Aisha", "Mohammed", "Fatima", "Omar", "Zainab", "Hassan",
    "Amina", "Ali", "Maya", "Sami", "Noor", "Yusuf", "Layla", "Ibrahim",
    "Sara", "Malik", "Yara", "Amir", "Nadia", "Karim", "Diana",
    
    # African names
    "Kwame", "Amina", "Kofi", "Zara", "Jabari", "Nala", "Tendai", "Zuri",
    "Kwesi", "Ashanti", "Nabil", "Kamau", "Ayanna", "Dikembe", "Makena",
    
    # Eastern European
    "Vladimir", "Natalia", "Dmitri", "Svetlana", "Nikolai", "Olga", "Ivan",
    "Elena", "Boris", "Irina", "Sergei", "Tatiana", "Andrei", "Anna",
    "Pavel", "Marina", "Mikhail", "Katya",
    
    # Nordic/Scandinavian
    "Lars", "Ingrid", "Erik", "Astrid", "Sven", "Elsa", "Nils", "Lena",
    "Olaf", "Freya", "Bjorn", "Saga", "Anders", "Linnea", "Henrik", "Karin",
    
    # French
    "Antoine", "Sophie", "Pierre", "Marie", "François", "Claire", "Louis",
    "Celine", "Henri", "Amelie", "Marc", "Camille", "Paul", "Emilie",
    "Jean", "Isabelle", "Luc", "Juliette",
    
    # German
    "Hans", "Anna", "Klaus", "Greta", "Wolfgang", "Hannah", "Heinz", "Elise",
    "Manfred", "Birgit", "Helmut", "Claudia", "Gunther", "Sabine",
    
    # Italian
    "Marco", "Sofia", "Alessandro", "Giulia", "Luca", "Francesca", "Giovanni",
    "Chiara", "Roberto", "Elena", "Daniele", "Valentina", "Stefano", "Alessia"
}

LAST_NAMES = {
    # Anglo/Western surnames
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Wilson",
    "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
    "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis",
    "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott",
    "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson",
    "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    
    # Hispanic/Latin American surnames
    "Gonzalez", "Rodriguez", "Fernandez", "Lopez", "Martinez", "Sanchez",
    "Perez", "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez", "Diaz",
    "Moreno", "Alvarez", "Munoz", "Romero", "Gutierrez", "Alonso",
    "Vargas", "Navarro", "Torres", "Dominguez", "Soto", "Castillo",
    "Ortega", "Ramos", "Guerrero", "Cruz", "Mendoza", "Vega", "Silva",
    
    # Asian surnames - Chinese
    "Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Zhao", "Huang", "Zhou",
    "Wu", "Xu", "Sun", "Ma", "Zhu", "Hu", "Guo", "He", "Gao", "Lin",
    "Lu", "Song", "Luo", "Han", "Xie", "Feng", "Jiang", "Cai", "Deng",
    
    # Asian surnames - Japanese
    "Tanaka", "Sato", "Suzuki", "Takahashi", "Watanabe", "Itō", "Yamamoto",
    "Nakamura", "Kobayashi", "Katō", "Yoshida", "Yamada", "Sasaki", "Yamaguchi",
    "Saito", "Matsumoto", "Inoue", "Kimura", "Hayashi", "Shimizu",
    
    # Asian surnames - Korean
    "Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Cho", "Yoon", "Jang",
    "Lim", "Han", "Shin", "Seo", "Kwak", "Ahn", "Song", "Moon", "Jeong",
    
    # Asian surnames - Indian
    "Patel", "Singh", "Kumar", "Sharma", "Shah", "Gupta", "Ali", "Khan",
    "Reddy", "Prasad", "Mehta", "Verma", "Jain", "Rao", "Iyer", "Nair",
    "Agarwal", "Malhotra", "Chopra", "Kapoor", "Naidu", "Desai", "Joshi",
    
    # Asian surnames - Vietnamese
    "Nguyen", "Tran", "Le", "Pham", "Hoang", "Huynh", "Phan", "Vu", "Vo",
    "Dang", "Bui", "Do", "Ho", "Ngo", "Duong", "Ly",
    
    # Middle Eastern surnames
    "Abdullah", "Hassan", "Ibrahim", "Khalil", "Malik", "Hussein", "Rahman",
    "Aziz", "Hamid", "Farid", "Shah", "Al-Mansoori", "Al-Rashid", "Omar",
    "Sayed", "Mahmoud", "Naser", "Qureshi", "Ansari", "Abbas", "Khan",
    
    # European surnames
    "Schmidt", "Muller", "Weber", "Fischer", "Meyer", "Schneider", "Wagner",
    "Becker", "Schulz", "Hoffman", "Schaefer", "Koch", "Bauer", "Richter",
    "Klein", "Schroeder", "Wolf", "Neumann", "Schwarz", "Zimmermann",
    
    # Italian surnames
    "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo",
    "Ricci", "Marino", "Greco", "Bruno", "Gallo", "Conti", "De Luca",
    "Costa", "Fontana", "Moretti", "Caruso", "Fabbri", "Rinaldi",
    
    # French surnames
    "Dubois", "Bernard", "Durand", "Petit", "Leroy", "Moreau", "Simon",
    "Laurent", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent",
    "Fournier", "Lefebvre", "Martinez", "Garnier", "Rousseau", "Bonnet",
    
    # Eastern European surnames
    "Ivanov", "Smirnov", "Kuznetsov", "Popov", "Sokolov", "Lebedev",
    "Kozlov", "Novikov", "Morozov", "Petrov", "Volkov", "Soloviev",
    "Savchenko", "Ivanova", "Kowalski", "Nowak", "Wiśniewski", "Dąbrowski",
    "Lewandowski", "Wójcik", "Kamiński", "Zieliński", "Szymański",
    
    # African surnames
    "Okoro", "Okafor", "Adebayo", "Nwankwo", "Mensah", "Osei", "Konaté",
    "Traoré", "Diallo", "Bah", "Abdullahi", "Ibrahim", "Hussein", "Ahmed",
    "Ochieng", "Kamau", "Wanjala", "Nzokoro", "Zulu", "Mthethwa"
}

CITIES = {
    # North America
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
    "San Francisco", "Seattle", "Denver", "Boston", "Baltimore", "Nashville",
    "Portland", "Las Vegas", "Miami", "Atlanta", "Toronto", "Montreal",
    "Vancouver", "Mexico City", "Guadalajara", "Monterrey", "Cancun",
    
    # Europe
    "London", "Paris", "Berlin", "Madrid", "Rome", "Amsterdam", "Barcelona",
    "Lisbon", "Vienna", "Prague", "Stockholm", "Oslo", "Copenhagen",
    "Dublin", "Edinburgh", "Brussels", "Warsaw", "Budapest", "Athens",
    "Istanbul", "Zurich", "Geneva", "Munich", "Hamburg", "Milan", "Naples",
    
    # Asia
    "Tokyo", "Osaka", "Kyoto", "Seoul", "Busan", "Shanghai", "Beijing",
    "Hong Kong", "Singapore", "Bangkok", "Kuala Lumpur", "Jakarta",
    "Manila", "Ho Chi Minh City", "Hanoi", "Mumbai", "Delhi", "Bangalore",
    "Chennai", "Kolkata", "Karachi", "Lahore", "Dubai", "Abu Dhabi",
    "Doha", "Riyadh", "Tel Aviv", "Jerusalem",
    
    # Oceania
    "Sydney", "Melbourne", "Brisbane", "Auckland", "Wellington", "Christchurch",
    
    # South America
    "São Paulo", "Rio de Janeiro", "Buenos Aires", "Santiago", "Lima",
    "Bogota", "Caracas", "Quito", "Montevideo", "La Paz",
    
    # Africa
    "Cairo", "Lagos", "Johannesburg", "Cape Town", "Nairobi", "Casablanca",
    "Accra", "Dakar", "Kigali", "Addis Ababa"
}

COUNTRIES = {
    "United States", "Canada", "United Kingdom", "France", "Germany",
    "Italy", "Spain", "Japan", "Australia", "Mexico", "Brazil", "India",
    "China", "South Korea", "Netherlands", "Switzerland", "Sweden",
    "Norway", "Denmark", "Finland", "Poland", "Ireland", "Portugal",
    "Greece", "Turkey", "Argentina", "Chile", "New Zealand", "Thailand",
    "Singapore", "Indonesia", "Malaysia", "Philippines", "Vietnam",
    "South Africa", "Egypt", "Morocco", "UAE", "Saudi Arabia", "Israel",
    "Croatia", "Iceland", "Peru", "Ecuador", "Colombia", "Costa Rica",
    "Panama", "Nicaragua", "Honduras", "Guatemala"
}

LANGUAGES = {
    "English", "Spanish", "French", "German", "Italian", "Portuguese",
    "Mandarin", "Japanese", "Korean", "Dutch", "Russian", "Arabic",
    "Polish", "Greek", "Turkish", "Hindi", "Swedish", "Norwegian",
    "Danish", "Finnish", "Vietnamese", "Thai", "Indonesian", "Malay",
    "Czech", "Romanian", "Hebrew", "Croatian", "Hungarian", "Bulgarian",
    "Serbian", "Slovak", "Ukrainian"
}

DESTINATIONS = {
    "Paris, France", "Tokyo, Japan", "New York City, USA", "London, UK",
    "Rome, Italy", "Barcelona, Spain", "Sydney, Australia", "Bali, Indonesia",
    "Santorini, Greece", "Dubai, UAE", "Machu Picchu, Peru", "Kyoto, Japan",
    "Prague, Czech Republic", "Amsterdam, Netherlands", "Marrakech, Morocco",
    "Istanbul, Turkey", "Seoul, South Korea", "Hong Kong, China",
    "Singapore, Singapore", "Cairo, Egypt", "Cape Town, South Africa",
    "Reykjavik, Iceland", "Lisbon, Portugal", "Vienna, Austria",
    "Budapest, Hungary", "Stockholm, Sweden", "Oslo, Norway",
    "Copenhagen, Denmark", "Edinburgh, Scotland", "Dublin, Ireland",
    "Venice, Italy", "Crete, Greece", "Maldives", "Bora Bora, French Polynesia",
    "Mauritius", "Seychelles", "Zanzibar, Tanzania", "Florence, Italy",
    "Cinque Terre, Italy", "Swiss Alps, Switzerland", "Lake Como, Italy",
    "Ibiza, Spain", "Mykonos, Greece", "Positano, Italy", "Amalfi Coast, Italy",
    "Banff, Canada", "Yellowstone, USA", "Grand Canyon, USA", "Yosemite, USA",
    "Patagonia, Argentina", "Galapagos, Ecuador"
}

PACKAGE_CATEGORIES = {
    "Adventure", "Luxury", "Budget", "Family", "Romantic", "Cultural",
    "Beach", "Mountain", "City Break", "Nature", "Wildlife", "History",
    "Food & Wine", "Wellness", "Spa", "Business", "Honeymoon", "Group Tours",
    "Solo Travel", "Family-Friendly", "Eco-Tourism", "Photography", "Religious",
    "Educational", "Hiking"
}

PACKAGE_NAMES = {
    "Weekend in Paris", "Tokyo Cultural Discovery", "New York City Break",
    "London Highlights Tour", "Roman Holiday", "Barcelona Escape",
    "Sydney Harbor Adventure", "Bali Paradise Retreat", "Santorini Sunset Experience",
    "Dubai Luxury Getaway", "Machu Picchu Trek", "Ancient Kyoto Journey",
    "Prague Castle Tour", "Amsterdam Canal Cruise", "Marrakech Souk Adventure",
    "Istanbul Bazaar Discovery", "Seoul Nightlife Tour", "Hong Kong Skyline Visit",
    "Singapore Gardens Tour", "Cairo Pyramids Expedition", "Cape Town Safari Experience",
    "Iceland Northern Lights", "Lisbon Food Tour", "Vienna Music Tour",
    "Budapest River Cruise", "Stockholm Archipelago", "Oslo Fjords Cruise",
    "Copenhagen Bike Tour", "Scottish Highlands", "Dublin Pub Crawl",
    "Venice Gondola Tour", "Greek Island Hopping", "Italian Wine Country",
    "Amalfi Coast Drive", "Swiss Alpine Adventure", "Patagonia Hiking",
    "Galapagos Wildlife", "Yellowstone National Park", "Grand Canyon Rafting",
    "Yosemite Camping", "European Grand Tour", "Asian Adventure",
    "South American Explorer", "African Safari", "Mediterranean Cruise",
    "Baltic Cruise", "Alaskan Adventure", "Canadian Rockies",
    "New Zealand South Island", "Iceland Ring Road", "Vietnam Backpacking"
}

PAYMENT_METHODS = {
    "Credit Card", "PayPal", "Bank Transfer", "Debit Card", "American Express",
    "Mastercard", "Visa", "Venmo", "Apple Pay", "Google Pay", "Cryptocurrency",
    "Traveler's Check", "Cash"
}

BOOKING_STATUS = {
    "Confirmed", "Pending", "Cancelled", "Waitlisted", "Refunded"
}

PAYMENT_STATUS = {"Completed", "Pending", "Failed", "Refunded", "Processing"}

SEASONS = {
    "Summer", "Winter", "Spring", "Fall", "Year-round", "Peak Season",
    "Off-Season"
}

CASE_TYPES = {
    "Customer Support", "Billing", "Technical Support", "Account Management", 
    "Product Feedback", "Booking Issue", "Cancellation Request", "Refund Request",
    "Payment Issue", "Travel Inquiry", "Complaint", "Other"
}

CASE_STATUS = {"Open", "In Progress", "Resolved", "Closed", "Pending"}

CASE_PRIORITY = {"Low", "Medium", "High", "Critical"}

CASE_SUBJECTS_BY_TYPE = {
    "Booking Issue": [
        "Unable to complete booking",
        "Booking confirmation not received",
        "Need to modify booking dates",
        "Package not available for selected dates",
        "Want to add travelers to existing booking",
        "Duplicate bookings created",
        "Booking shows incorrect information",
        "Need to transfer booking",
        "Promotional code not working",
        "Special requests not recorded",
        "Package upgrade request",
        "Group booking inquiry",
    ],
    
    "Payment Issue": [
        "Payment failed but amount deducted",
        "Payment method not working",
        "Incorrect amount charged",
        "URGENT: Double charge on account",
        "Payment method declined",
        "Currency conversion issue",
        "Payment plan not processing",
        "Transaction failed unexpectedly",
        "URGENT: Multiple unauthorized charges",
        "CRITICAL: Fraudulent transaction on account",
    ],
    
    "Billing": [
        "Request invoice for payment",
        "Invoice shows incorrect amount",
        "Need detailed billing breakdown",
        "VAT receipt request",
        "Billing address update",
        "Hidden fees inquiry",
        "Tax refund question",
        "Receipt reissue needed",
    ],
    
    "Account Management": [
        "Cannot access account",
        "Need to update personal information",
        "Loyalty points not reflecting",
        "Want to merge duplicate accounts",
        "Email not receiving notifications",
        "Account locked issue",
        "Password reset not working",
        "Profile update needed",
        "Account security concern",
        "Two-factor authentication issue",
    ],
    
    "Travel Inquiry": [
        "Question about destination",
        "Need travel insurance information",
        "Visa requirements inquiry",
        "Vaccination requirements",
        "Weather information request",
        "Local customs inquiry",
        "Destination recommendations",
        "Travel documentation needed",
        "Airport transfer information",
        "Local transportation inquiry",
    ],
    
    "Cancellation Request": [
        "Request booking cancellation",
        "Cancellation policy question",
        "URGENT: Emergency cancellation needed",
        "URGENT: Medical emergency cancellation",
        "Work conflict cancellation",
        "URGENT: Family emergency cancellation",
        "Travel advisory cancellation",
        "Partial group cancellation",
        "Weather-related cancellation",
        "URGENT: Death in family - immediate cancellation",
        "Emergency situation requiring cancellation",
    ],
    
    "Refund Request": [
        "Refund status inquiry",
        "Unable to process refund",
        "URGENT: Refund amount disputed",
        "URGENT: Expedited refund request needed",
        "Partial refund request",
        "URGENT: Refund not received after 30 days",
        "Travel credit instead of refund",
        "Insurance claim refund",
        "CRITICAL: Large refund amount missing",
    ],
    
    "Technical Support": [
        "Website not loading properly",
        "Mobile app crashing",
        "Cannot upload documents",
        "Search function not working",
        "Payment page error",
        "App sync issue",
        "Email links not working",
        "Booking confirmation not accessible",
    ],
    
    "Complaint": [
        "Complaint about service",
        "Accommodation quality issue",
        "Staff behavior complaint",
        "Misleading package description",
        "Amenities not available",
        "Poor service experience",
        "Cleanliness issue",
        "URGENT: Safety concern - immediate attention needed",
        "Service not as advertised",
        "URGENT: Health and safety emergency",
        "CRITICAL: Unsafe conditions at property",
        "Severe service failure",
    ],
    
    "Customer Support": [
        "General travel advice",
        "Special accommodation request",
        "Dietary restriction inquiry",
        "Accessibility needs",
        "Special assistance required",
        "Communication preference update",
        "Emergency contact needed",
        "Language support request",
    ],
    
    "Product Feedback": [
        "Feedback on recent trip",
        "Service improvement suggestion",
        "Website usability feedback",
        "Package recommendation",
        "New feature request",
        "Review submission",
        "General feedback",
    ],
    
    "Other": [
        "Corporate travel inquiry",
        "Documentation request",
        "Insurance certificate needed",
        "Travel history report",
        "Verification letter needed",
        "Legal documentation required",
        "Emergency assistance",
        "General inquiry",
    ],
}

AGENT_NAMES = {
    "Sarah Johnson", "Michael Chen", "Emily Rodriguez", "David Kim",
    "Jessica Patel", "Robert Taylor", "Amanda Singh", "James Wilson",
    "Maria Garcia", "Christopher Lee", "Jennifer Brown", "Daniel Martinez",
    "Lisa Anderson", "Matthew Thomas", "Ashley White", "Joshua Miller"
}

# Street names for addresses
STREET_NAMES = {
    # Classic street names
    "Main Street", "First Street", "Second Street", "Third Street", "Fourth Street",
    "Fifth Avenue", "Sixth Avenue", "Seventh Street", "Eighth Avenue", "Ninth Street",
    "Tenth Avenue", "Broadway", "Market Street", "Church Street", "School Street",
    "Water Street", "Mill Street", "King Street", "Queen Street", "High Street",
    "Center Street", "State Street", "Court Street", "Union Street", "Liberty Street",
    
    # Tree-themed streets
    "Oak Avenue", "Elm Street", "Maple Drive", "Cedar Lane", "Pine Street",
    "Willow Road", "Birch Avenue", "Ash Street", "Cherry Lane", "Walnut Drive",
    "Spruce Avenue", "Poplar Street", "Magnolia Drive", "Cypress Lane", "Hickory Road",
    "Sycamore Street", "Dogwood Avenue", "Redwood Drive", "Palm Boulevard", "Aspen Way",
    
    # Presidential/Historical streets
    "Washington Street", "Lincoln Avenue", "Jefferson Road", "Madison Avenue",
    "Monroe Drive", "Adams Street", "Jackson Street", "Roosevelt Boulevard",
    "Kennedy Drive", "Grant Avenue", "Wilson Street", "Franklin Road",
    "Hamilton Street", "Lafayette Avenue", "Lee Street", "King Boulevard",
    
    # Nature-themed streets
    "Park Avenue", "Forest Lane", "Garden Avenue", "River Road", "Lake Street",
    "Hill Street", "Mountain View Drive", "Valley Road", "Meadow Lane", "Ridge Avenue",
    "Creek Drive", "Brook Street", "Canyon Road", "Summit Avenue", "Highland Avenue",
    "Woodland Drive", "Prairie Avenue", "Plains Road", "Mesa Drive", "Desert Lane",
    
    # Seasonal/Time streets
    "Spring Street", "Summer Avenue", "Autumn Lane", "Winter Boulevard",
    "Sunrise Drive", "Sunset Way", "Moonlight Lane", "Twilight Drive", "Dawn Street",
    "Dusk Avenue", "Morning Glory Lane", "Evening Star Drive",
    
    # Directional streets
    "North Street", "South Avenue", "East Street", "West Drive", "Central Avenue",
    
    # Water-themed streets
    "Riverside Drive", "Lakeside Drive", "Ocean Drive", "Beach Road", "Harbor Street",
    "Bay Avenue", "Shore Drive", "Coastline Road", "Marina Boulevard", "Seaside Avenue",
    "Wharf Street", "Dock Road", "Pier Avenue", "Coral Drive", "Wave Street",
    
    # Flower-themed streets
    "Rose Avenue", "Lily Lane", "Violet Street", "Iris Drive", "Daisy Court",
    "Tulip Street", "Orchid Avenue", "Jasmine Lane", "Lavender Road", "Peony Drive",
    "Sunflower Street", "Marigold Avenue", "Gardenia Lane", "Azalea Drive",
    
    # Color-themed streets
    "Green Street", "Blue Ridge Road", "Silver Avenue", "Golden Gate Drive",
    "Amber Lane", "Ruby Street", "Emerald Avenue", "Pearl Drive", "Diamond Street",
    
    # Classic British/European streets
    "Victoria Avenue", "Albert Street", "Windsor Drive", "Cambridge Road",
    "Oxford Avenue", "Wellington Street", "Nelson Road", "Churchill Drive",
    "George Street", "Elizabeth Avenue", "Charles Street", "Royal Avenue",
    
    # Modern/Descriptive streets
    "Chestnut Street", "Pleasant Street", "Fairview Avenue", "Hillside Drive",
    "Valley View Road", "Clearwater Drive", "Greenwood Avenue", "Northgate Boulevard",
    "Southgate Drive", "Westgate Road", "Eastgate Avenue", "Heritage Lane",
    "Legacy Drive", "Harmony Street", "Peaceful Lane", "Serenity Drive",
    "Tranquil Way", "Prosperity Avenue", "Victory Boulevard", "Commerce Street",
    "Industrial Drive", "Technology Way", "Innovation Drive", "Progress Avenue",
    
    # International flavor
    "Via Roma", "Rue de Paris", "Calle Principal", "Avenida Central",
    "Strada Nuova", "Camino Real", "Plaza Drive", "Paseo del Sol",
    
    # Numbered avenues (for variation)
    "11th Street", "12th Avenue", "15th Street", "20th Avenue", "25th Street",
    "30th Avenue", "42nd Street", "50th Avenue", "100th Street"
}

# Phone number templates (will be filled with random digits)
PHONE_FORMATS = {
    "(555) {}-{}", "(555) {}-{}", "+1-555-{}-{}", "555.{}.{}", "{}555{}"
}

# Import organized case descriptions
from .case_descriptions import CASE_DESCRIPTIONS_BY_TYPE

# Export commonly used variables
__all__ = [
    'FIRST_NAMES', 'LAST_NAMES', 'CITIES', 'COUNTRIES', 'LANGUAGES',
    'DESTINATIONS', 'PACKAGE_CATEGORIES', 'PACKAGE_NAMES',
    'PAYMENT_METHODS', 'BOOKING_STATUS', 'PAYMENT_STATUS', 'SEASONS',
    'CASE_TYPES', 'CASE_STATUS', 'CASE_PRIORITY', 'CASE_SUBJECTS_BY_TYPE',
    'AGENT_NAMES', 'STREET_NAMES', 'PHONE_FORMATS', 'CASE_DESCRIPTIONS_BY_TYPE'
]
