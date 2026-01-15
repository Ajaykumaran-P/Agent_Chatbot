from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google_agent.agent import google_agent
from typing import Dict


def personal_information() -> dict:
    """
       Get the user personal details like department name,hod detailes, overview,vision and mission .
    """
    return{
        

    "it": {
        "department_name": "Information Technology",
        "established_year": 1998,
        "hod": {
            "name": "Dr. P. Shenbagam",
            "designation": "Assistant Professor III",
            "email": "shenbagam.p.it@kct.ac.in"
        },
        "overview": (
            "The IT Department focuses on quality education and skill development. "
            "Key areas include Artificial Intelligence, Data Science, IoT, and Cybersecurity. "
            "The department achieves over 95 percent placements annually."
        ),
        "vision": (
            "To become a school of excellence in Information Technology education and research."
        ),
        "mission": (
            "Provide practice-based learning, encourage research, promote social responsibility, "
            "and entrepreneurship."
        )
    },

    "cse": {
        "department_name": "Computer Science and Engineering",
        "established_year": 1987,
        "hod": {
            "name": "Dr. E. A. Vimal",
            "designation": "Associate Professor",
            "email": "vimal.ea.cse@kct.ac.in"
        },
        "overview": (
            "The department offers UG, PG, and PhD programs. "
            "Focus areas include AI, Data Science, IoT, Cybersecurity, Web Development, "
            "Extended Reality, and Automation."
        ),
        "vision": (
            "To evolve as a center of excellence in Computer Science and Engineering."
        ),
        "mission": (
            "Industry readiness, professional development, ethical values, "
            "leadership, and entrepreneurship."
        )
    },

    "ae": {
        "department_name": "Aeronautical Engineering",
        "established_year": None,
        "hod": {
            "name": "Dr. M. Senthilkumar",
            "designation": "Assistant Professor III",
            "email": "hod.aero@kct.ac.in"
        },
        "overview": (
            "The department provides education in Aerodynamics, Aircraft Structures, Propulsion, "
            "Flight Mechanics, Avionics, and UAV. Students gain exposure through internships in "
            "HAL, NAL, ADA, ADE, and DRDO."
        ),
        "vision": (
            "To attain excellence and global reputation in Aeronautical Engineering education and research."
        ),
        "mission": (
            "Provide quality education, promote research, interdisciplinary learning, "
            "and industry collaboration."
        )
    },

    "ate": {
        "department_name": "Automobile Engineering",
        "established_year": 2011,
        "hod": {
            "name": "Dr. J. D. Andrew Pon Abraham",
            "designation": "Assistant Professor II",
            "email": "andrew.auto@kct.ac.in"
        },
        "overview": (
            "The department focuses on Automotive Design, Automotive Electronics, and Service. "
            "Major research areas include Hybrid and Electric Vehicles, Vehicle Design, "
            "and Performance Optimization."
        ),
        "vision": (
            "To be a renowned learning centre in Automobile Engineering."
        ),
        "mission": (
            "Develop industry-ready graduates, promote social responsibility, "
            "and encourage entrepreneurship."
        )
    },

    "be": {
        "department_name": "Biotechnology",
        "established_year": 2002,
        "hod": {
            "name": "Dr. Vinohar Stephen Rapheal",
            "designation": "Associate Professor",
            "email": "vinohar.stephenrapheal.bt@kct.ac.in"
        },
        "overview": (
            "The department offers B.Tech, M.Tech, and PhD programs. "
            "Key focus areas include Healthcare, Nutrition, Bioprocess Technology, "
            "and Environmental Biotechnology."
        ),
        "vision": (
            "To build strong teaching and research foundations in biotechnology and allied fields."
        ),
        "mission": (
            "Promote innovation, startups, leadership skills, and social welfare "
            "through biotechnology education."
        )
    },

    "ece": {
        "department_name": "Electronics & Communication Engineering",
        "established_year": 1986,
        "hod": {
            "name": "Dr. M. Bharathi",
            "designation": "Professor",
            "email": "bharathi.m.ece@kct.ac.in"
        },
        "overview": (
            "The department has advanced labs including DSP, VLSI, RF, Optical, and Microwave labs. "
            "Focus areas include Signal Processing, Communication Systems, Machine Learning, and VLSI."
        ),
        "vision": (
            "To be a centre of repute for learning and research with global standards."
        ),
        "mission": (
            "Develop professional ethics, innovation, leadership, and excellence "
            "in academics and research."
        )
    },

    "eie": {
        "department_name": "Electronics & Instrumentation Engineering",
        "established_year": 2006,
        "hod": {
            "name": "Dr. V. Dinesh Kumar",
            "designation": "Associate Professor",
            "email": "dineshkumar.v.eie@kct.ac.in"
        },
        "overview": (
            "The department focuses on Instrumentation, Process Control, PLC, SCADA, DCS, and Automation. "
            "It has industry collaborations and advanced laboratories including Siemens PLC and Edge AI labs."
        ),
        "vision": (
            "To transform learners into responsible engineers solving industry and societal problems."
        ),
        "mission": (
            "Promote modern teaching, research, automation skills, higher studies, "
            "and lifelong learning."
        )
    },

    "ce": {
        "department_name": "Civil Engineering",
        "established_year": None,
        "hod": {
            "name": "Dr. V. Gayathri",
            "designation": "Professor & Head",
            "email": None
        },
        "overview": (
            "The Department of Civil Engineering is one of the earliest departments of Kumaraguru College of Technology. "
            "It specializes in Structural Engineering, Environmental and Water Resources, Construction Management, "
            "Geotechnology, Transportation, Geoinformatics, and Coastal Engineering."
        ),
        "vision": (
            "To become a world-class academic centre for quality education and research in diverse areas "
            "of Civil Engineering with strong social commitment."
        ),
        "mission": (
            "Producing highly competent professionals. Providing quality education with strong ethics. "
            "Developing research leading to practical applications and offering consultancy services."
        )
    },

    "eee": {
        "department_name": "Electrical and Electronics Engineering",
        "established_year": 1984,
        "hod": {
            "name": "Dr. P. Thirumoorthi",
            "designation": "Professor & Head",
            "email": None
        },
        "overview": (
            "The department offers UG and PG programmes in Electrical and Electronics Engineering "
            "and Embedded Systems Technologies. Major thrust areas include Electrical Machines, "
            "Power Electronics, Power Systems, Electric Vehicles, Renewable Energy, and Industrial IoT."
        ),
        "vision": (
            "To be a Centre of Excellence in globalizing education and research in Electrical and Electronics Engineering."
        ),
        "mission": (
            "Empower students with state-of-the-art knowledge. Emphasize leadership and social values. "
            "Enable impactful research and innovation."
        )
    },

    "ft": {
        "department_name": "Fashion Technology",
        "established_year": 2002,
        "hod": {
            "name": "Dr. R. Priyadarshini",
            "designation": "Assistant Professor III & Head",
            "email": None
        },
        "overview": (
            "The department equips students with competencies in Clothing Technology and Fashion. "
            "It emphasizes sustainability, eco-fashion, circular processing, and high-performance apparel."
        ),
        "vision": (
            "To achieve excellence in academics and research in the fashion and clothing industry."
        ),
        "mission": (
            "Develop design, manufacturing, and management skills. Enhance faculty expertise. "
            "Promote creativity, responsibility, and industry collaboration."
        )
    },

    "me": {
        "department_name": "Mechanical Engineering",
        "established_year": 1984,
        "hod": {
            "name": "Dr. P. S. Samuel Ratna Kumar",
            "designation": "Assistant Professor III & Head",
            "email": None
        },
        "overview": (
            "The department is NBA accredited and recognized as a research centre by Anna University. "
            "It follows ASME-aligned curriculum and emphasizes sustainable engineering practices."
        ),
        "vision": (
            "To achieve global recognition by promoting innovation, sustainability, and leadership."
        ),
        "mission": (
            "Promote innovation and ethics. Create active learning ecosystems. "
            "Facilitate impactful research in mechanical systems."
        )
    },

    "mct": {
        "department_name": "Mechatronics Engineering",
        "established_year": 1999,
        "hod": {
            "name": "Dr. M. Saravana Mohan",
            "designation": "Associate Professor & Head",
            "email": None
        },
        "overview": (
            "The department bridges industry and academia with strong laboratory infrastructure "
            "and interdisciplinary expertise in Mechanical, Electronics, and Mechatronics engineering."
        ),
        "vision": (
            "To achieve excellence in academic and industrial automation research."
        ),
        "mission": (
            "Impart interdisciplinary skills. Motivate research for global needs. "
            "Promote innovation with social responsibility."
        )
    },

    "te": {
        "department_name": "Textile Engineering",
        "established_year": 1995,
        "hod": {
            "name": "Dr. M. Saravanan",
            "designation": "Assistant Professor III & Head",
            "email": None
        },
        "overview": (
            "The department supports the textile industry with modern laboratories, "
            "experienced faculty, and strong industry collaborations."
        ),
        "vision": (
            "To be a Centre of Excellence in Textile Technology and Management."
        ),
        "mission": (
            "Develop industry-relevant curriculum. Encourage faculty development. "
            "Support entrepreneurship and interdisciplinary research."
        )
    },

    "ca": {
        "department_name": "Computer Applications",
        "established_year": 1993,
        "hod": {
            "name": "Dr. V. Vijilesh",
            "designation": "Associate Professor & Head",
            "email": None
        },
        "overview": (
            "The department focuses on developing computational skills required by the IT industry "
            "with modern laboratories and experienced faculty."
        ),
        "vision": (
            "To be a leader in computing education and research."
        ),
        "mission": (
            "Deliver quality education and practical skills. Encourage innovation and research. "
            "Nurture ethical and socially responsible professionals."
        )
    }



   

    },



student_agent= LlmAgent(
    name="support_chatbot",
    model="gemini-2.5-flash",
    description="A friendly student support chatbot that provides common information about the college and its departments.",
    instruction="""
You are a friendly and helpful assistant.

Answer user questions using the following priority:
1. FIRST, try to answer using the personal_information tool (college dataset).
2. IF the required information is NOT found in the dataset,
   THEN use the google_search tool to search the web.

Rules:
- Do NOT guess.
- Prefer personal_information whenever the question is about college or departments.
- Use google_search only as a fallback.
- Respond clearly and politely.
""",


    tools=[personal_information,AgentTool(google_agent)]


)

root_agent = student_agent