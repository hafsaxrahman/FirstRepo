import tkinter as tk
import random as rand
from tkinter import messagebox as msgbox
from tkinter import ttk



# App
app = tk.Tk()
app.title ("Basic First Aid App")
app.geometry ("1300x700")




# Color scheme
color_blue = "#4da6ff"
color_green = "#b3ffb3"
color_white = "white" #fileapp online edited for push




# Initializing frames
header_frame = tk.Frame(app, bg = color_blue, height = 60 )
header_frame.pack (fill = "x")

button_frame = tk.Frame(app, bg = color_green, width = 500)
button_frame.pack (fill = "y", side = "left")

checklist_frame = tk.Frame(app, bg = color_green, width = 200)
checklist_frame.pack (fill="y", side = "right")

content_frame = tk.Frame(app, bg = color_white, width = 700)
content_frame.pack (fill ="both", side = "left", expand = True)




#Header Label
header_label = tk.Label(header_frame, text = "FIRST AID GUIDE", font =("Helvetica", 35, "bold"),
                        bg= color_blue, fg= color_white,)

header_label.pack(fill = "x")



#data-set
INJURIES = \
{
    "Cuts":
    {
        "Severe": [
            "Apply firm pressure with a clean cloth or bandage to control bleeding.",
            "Elevate the affected area if possible.",
            "Seek immediate medical help if the bleeding is heavy or does not stop."],

        "Mild":
        [
            "Clean the wound with clean water to remove debris.",
            "Apply pressure with a sterile cloth or gauze until bleeding stops.",
            "Dress the wound with an antiseptic and a sterile bandage."
        ],

        "Low":
        [
            "Rinse the wound under clean water.",
            "Gently pat the area dry with a clean cloth.",
            "Apply antiseptic ointment and cover with a bandage."
        ],

    },
    "Burns":
    {
        "Severe":
        [
            "Do not apply ice or cold water directly on the burn.",
            "Cover with a sterile, non-stick bandage to prevent infection.",
            "Seek immediate medical assistance."
        ],

        "Mild":
        [
            "Run cool (not cold) water over the burn for at least 10 minutes.",
            "Gently pat the area dry and apply a sterile bandage.",
            "Avoid breaking blisters; seek medical attention if needed."
        ],

        "Low":
        [
            "Cool the burn with cold water for several minutes.",
            "Apply a soothing aloe vera or burn ointment.",
            "Cover lightly with a bandage to prevent irritation."
        ],

    },
    "Insect Bite/Sting":
    {
        "Severe":
        [
            "Administer epinephrine if available.",
            "Call emergency services immediately.",
            "Keep the person calm and monitor until help arrives."
        ],

        "Mild":
        [
            "Clean the area with antiseptic to prevent infection.",
            "Monitor for any signs of worsening symptoms."
        ],

        "Low":
        [
            "Apply ice or a cold compress to reduce swelling.",
            "Keep the affected area clean and avoid scratching."
        ],

    },
    "Nosebleed":
    {
        "Severe":
        [
            "Apply pressure by pinching nostrils and leaning forward.",
            "Seek immediate medical help if bleeding continues."
        ],

        "Mild":
        [
            "Tilt the head forward slightly (do not tilt back).",
            "Pinch nostrils firmly and apply pressure for several minutes.",
            "Once bleeding stops, avoid touching the nose for a while."
        ],

        "Low":
        [
            "Sit down calmly and pinch the nose.",
            "Apply slight pressure and breathe through the mouth.",
            "Wait for bleeding to stop; avoid blowing your nose afterward."
        ],

    },
    "Sprain":
    {
        "Severe":
        [
            "Do not attempt to move the injured area.",
            "Seek medical assistance promptly.",
            "Immobilize the area and keep it elevated."
        ],

        "Mild":
        [
            "Apply ice to the area in intervals (20 minutes on, 20 minutes off).",
            "Rest and elevate the sprained area to reduce swelling."
        ],

        "Low":
        [
            "Rest and apply a compression bandage if available.",
            "Use ice to manage swelling and avoid putting weight on the area."
        ],

    },
    "Fracture":
    {
        "Severe":
        [
            "Do not move the injured limb or apply pressure.",
            "Cover any open wound with a clean cloth or gauze.",
            "Seek immediate medical assistance."
        ],

        "Mild":
        [
            "Gently immobilize the area with a splint or makeshift support.",
            "Apply ice packs to reduce pain and swelling."
        ],

        "Low":
        [
            "Support and rest the injured area.",
            "Avoid putting weight on the area and consult a medical professional."
        ],

    },
    "Allergic Reactions":
    {
        "Severe":
        [
            "Administer epinephrine if available.",
            "Call emergency services immediately.",
            "Keep the person calm and monitor for worsening symptoms."
        ],

        "Mild":
        [
            "Take antihistamines (like Benadryl) to reduce symptoms.",
            "Monitor closely for signs of escalation."
        ],

        "Low":
        [
            "Avoid further contact with the allergen.",
            "Apply a cool compress if there is slight itching or swelling.",
            "Monitor symptoms and take an antihistamine if needed."
        ]

    }
}




CONDITIONS =\
{
    "Asthma":
    {
        "Description": "A condition that causes breathing difficulty due to narrowed airways.",
        "Steps":
        [
            "Assist the individual in using their inhaler if they have one available.",
            "Help them sit upright and stay calm to make breathing easier.",
            "Encourage slow, deep breaths if possible.",
            "Call emergency services if symptoms don’t improve or if the person appears to be in distress."
        ]
    },
    "Diabetes":
    {
        "Description": "A condition where the body has difficulty regulating blood sugar levels.",
        "Steps":
        [
            "If the person is experiencing low blood sugar (hypoglycemia), provide them with a sugary snack or drink.",
            "Assist them in monitoring their blood sugar levels if they have the necessary equipment.",
            "Encourage them to rest and avoid exertion until their blood sugar stabilizes.",
            "Call emergency services if they are unresponsive, confused, or if blood sugar levels do not improve with treatment."
        ]
    },
    "Seizures":
    {
        "Description": "A sudden, uncontrolled electrical disturbance in the brain, which can cause changes in behavior, movements, or consciousness.",
        "Steps":
        [
            "Do not restrain the person or attempt to stop their movements.",
            "Clear the area of any hard or sharp objects that could cause injury.",
            "Place something soft under their head to protect it from impact.",
            "Roll them onto their side once the seizure ends to help keep the airway clear.",
            "Call emergency services if the seizure lasts more than 5 minutes or if another seizure follows immediately."
        ]
    }
}




TREATMENT_PLANS = \
{
    "R.I.C.E. (Rest, Ice, Compression, Elevation)":
    {
        "Description": "A method for treating sprains, strains, and similar soft tissue injuries to reduce pain and swelling.",
        "Steps":
        [
            "Rest: Avoid using the injured area to prevent further damage.",
            "Ice: Apply an ice pack (wrapped in a cloth) to the injured area for 15-20 minutes every hour to reduce swelling.",
            "Compression: Use an elastic bandage to compress the area, which helps control swelling.",
            "Elevation: Raise the injured limb above heart level whenever possible to reduce swelling."
        ]
    },
    "CPR (Cardiopulmonary Resuscitation)":
    {
        "Description": "An emergency procedure for someone in cardiac arrest to manually restore blood circulation and breathing.",
        "Steps":
        [
            "Check for responsiveness by gently shaking the person and asking if they’re okay.",
            "If unresponsive and not breathing, begin CPR immediately.",
            "Give 30 chest compressions, pressing down at least 2 inches at a rate of 100-120 compressions per minute.",
            "After compressions, give 2 rescue breaths by tilting the head back, lifting the chin, and breathing into the person's mouth.",
            "Repeat the cycle of 30 compressions and 2 breaths until help arrives or the person begins breathing on their own."
        ]
    }
}





#checklist initialisation

checklist_items = \
    [
        "Gauze", "Bandages", "Medical Tape", "Scissors", "Tweezers", "Antiseptic", "Pain Reliever",
        "Gloves","Burn Ointment", "Ibuprofen", "Hot Pack", "Cold Pack"

    ]

checklist_dict = {}

#Emergency Numbers

emergency_contact = \
    { "Ambulance":"1012" }


# Function to create sidebar buttons
def create_sidebar_buttons():
    sidebar_buttons = ['Injuries', 'Conditions', 'Treatment Plans', 'Emergency Contacts']
    for section in sidebar_buttons:
        button = tk.Button( button_frame, text=section, width=25, height=3, bg=color_white, font=("Helvetica", 14),
                            command=lambda sec=section: display_section_content(sec))
        button.pack(pady=10)


# Helper function to clear content frame
def clear_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()


# Function to display injuries
def display_injuries():
    clear_content_frame()
    for injury in INJURIES:
        button = tk.Button(content_frame, text=injury,width=30,height=2, font=("Helvetica", 12),bg=color_blue, fg=color_white,
                           command=lambda inj=injury: display_severity_buttons(inj))
        button.pack(pady=10)


# Function to display severity levels for a selected injury
def display_severity_buttons(injury):
    clear_content_frame()
    tk.Label(content_frame, text=f"Severity for {injury}", font=("Helvetica", 18, "bold"), bg=color_white ).pack(pady=10)

    severities = ['Severe', 'Mild', 'Low']
    for severity in severities:
        button = tk.Button(content_frame,text=severity,width=20,height=2,
                           command=lambda sev=severity: display_injury_info(sev, injury))
        button.pack(pady=5)


# Function to display injury information
def display_injury_info(severity, injury):
    clear_content_frame()
    tk.Label( content_frame,text=f"Treatment for {injury} (Severity: {severity})", font=("Helvetica", 18, "bold"),bg=color_white).pack(pady=10)

    for step in INJURIES[injury][severity]:
        tk.Label(content_frame, text=step, font=("Helvetica", 12), bg=color_white).pack(anchor="w", padx=20)


# Function to display conditions
def display_conditions():
    clear_content_frame()
    for condition, details in CONDITIONS.items():
        tk.Label(content_frame, text=condition, font=("Helvetica", 18, "bold"), bg = color_white).pack(pady=10)
        tk.Label(content_frame, text=details["Description"], font=("Helvetica", 12), bg=color_white).pack(pady=5)
        for step in details["Steps"]:
            tk.Label(content_frame, text=step, font=("Helvetica", 10), bg=color_white).pack(anchor="w", padx=20)


# Function to display treatment plans
def display_treatment_plans():
    clear_content_frame()
    for plan, details in TREATMENT_PLANS.items():
        tk.Label(content_frame, text=plan, font=("Helvetica", 18, "bold"), bg=color_white).pack(pady=10)
        tk.Label(content_frame, text=details["Description"], font=("Helvetica", 12), bg=color_white).pack(pady=5)
        for step in details["Steps"]:
            tk.Label(content_frame, text=step, font=("Helvetica", 10), bg=color_white).pack(anchor="w", padx=20)


# Function to display emergency contacts
def display_emergency_contacts():
    clear_content_frame()
    for contact, number in emergency_contact.items():
        tk.Label(content_frame, text=f"{contact}: {number}", font=("Helvetica", 14), bg=color_white).pack(pady=10)


# Function to create checklist
def create_checklist():
    for item in checklist_items:
        checkbox = tk.Checkbutton( checklist_frame, text=item, font=("Helvetica", 12), bg=color_green )
        checkbox.pack(anchor="w", padx=20, pady=5)



# Function to display content for a specific section
def display_section_content(section):
    if section == 'Injuries':
        display_injuries()
    elif section == 'Conditions':
        display_conditions()
    elif section == 'Treatment Plans':
        display_treatment_plans()
    elif section == 'Emergency Contacts':
        display_emergency_contacts()




# Initialize the app
create_sidebar_buttons()
create_checklist()
app.mainloop()
