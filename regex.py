import re

text = """ Subject: Conference Registration Confirmation - NLP2024

Dear Dr. Sarah Chen,

Thank you for registering for the International Conference on Natural Language Processing (NLP2024). Here are your registration details:

Conference Dates: March 15-17, 2024
Registration Time: 9:00 AM - 5:30 PM daily
Location: Stanford University, California

Your confirmation number is: NLP-2024-7829
Registration fee: $450.00 (paid via credit card ending in 4521)
Student discount applied: -$125.50
Total amount: $324.50

Please contact our support team if you have any questions:
- Email: support@nlp2024conference.org
- Alternative contact: info@conference-nlp.edu
- Phone: +1 (650) 723-2300
- International: +44 20 7946 0958
- Fax: 650.725.1449

Important reminders:
• Check-in opens at 8:30 AM on March 15th, 2024
• The keynote speech begins at 10:15 AM
• Lunch will be served from 12:00 PM to 1:30 PM
• Coffee breaks: 3:15 PM - 3:45 PM

Workshop submissions are due by February 28, 2024 at 11:59 PM PST. Late submissions will incur a $75 processing fee.

For hotel bookings, contact:
Grand Hotel Stanford: (650) 493-2000
Budget Inn: 650-321-9900
Conference rate: $89/night (valid until Feb 14, 2024)

Financial aid applications should be sent to grants@nlp-conference.org by Jan 31, 2024. Maximum award: €1,200 or £950.

Please visit our website at https://www.nlp2024conference.org for updates. You can also follow us on social media:
- Twitter: @NLP2024conf
- LinkedIn: linkedin.com/company/nlp2024
- GitHub: github.com/nlp2024/conference-materials

Emergency contact during the conference: Dr. Michael Rodriguez at m.rodriguez@stanford.edu or call (650) 555-0123.

Additional information available at:
- Conference portal: https://portal.nlp2024conference.org/dashboard
- Paper submissions: http://submissions.nlp2024.edu/login
- Accommodation: www.stanford.edu/visitors/hotels

Payment confirmation sent to: s.chen@university.ac.uk
Backup email: sarah.chen.nlp@gmail.com

Best regards,
The NLP2024 Organization Committee

---

P.S. Don't forget to bring your ID and confirmation email. For questions about dietary restrictions, contact catering@conference.org before March 10, 2024.

Conference hotline: 1-800-NLP-2024 (1-800-657-2024)
Text support: Send SMS to (650) 555-TEXT

Refund policy: Full refunds available until Feb 1st, 2024. After this date, a $50.00 cancellation fee applies."""

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)
print(emails)

ph_numbers_1 = re.findall(r'\+\d{2,4}[\s|-]+\d{2,4}[\s|-]+\d{4}[\s|-]+\d{4}', text)
print(ph_numbers_1)

ph_numbers_2 = re.findall(r'\+\d[\s]\(\d{1,3}\)[\s]\d{1,3}\-\d{1,4}', text)
print(ph_numbers_2)

ph_numbers_3 = re.findall(r'[\(|\d{1,3}]+[\d{1,3}|\)][\s|\-]\d{1,3}\-\d{1,4}[/$|\-\d{1,4}\)]', text)
print(ph_numbers_3)

ph_numbers_4 = re.findall(r'\(?\d{1}?\-?\(?\d{1,3}\)?[ |\-]\d{3}\-\d{4}\)?', text)
print(ph_numbers_4)

urls = re.finditer(r'((https://)|(www.)|(http://)|(\w+\.com))\/?[A-Za-z]+\.?\/?[A-Za-z0-9]+\.?\/?[A-Za-z0-9]+\/?[A-Za-z0-9]+', text)
print([url.group() for url in urls])
