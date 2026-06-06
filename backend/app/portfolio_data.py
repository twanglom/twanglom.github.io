PROFILE = {
    "name": "Thanasak Wanglomklang",
    "title": "Mechanical Engineering | Physics-AI Researcher",
    "subtitle": "Mechanical engineer connecting system dynamics, measured signals, and computational modeling",
    "location": "Fukuoka, Japan",
    "email": "thanasak.wang@gmail.com",
    "summary": (
        "Mechanical engineer and Physics-AI researcher connecting system "
        "dynamics, measured signals, and computational modeling to solve "
        "practical engineering problems. Background spans precision automation, "
        "vibration diagnostics, physics-based simulation, and uncertainty-aware "
        "optimization across manufacturing, acoustics, aerodynamics, and "
        "materials design. Develops interpretable workflows and software tools "
        "that turn sensor data and high-fidelity simulations into design insight, "
        "diagnostic decisions, and validated research outcomes."
    ),
    "cvUrl": "/cvfiles/CV-THANASAK-2026.pdf",
    "imageUrl": "/profile-1.JPG",
    "links": [
        {"label": "GitHub", "href": "https://github.com/twanglom"},
        {"label": "LinkedIn", "href": "https://www.linkedin.com/in/thanasak-wanglomklang-6797362aa"},
        {"label": "Email", "href": "mailto:thanasak.wang@gmail.com"},
    ],
    "highlights": [
        "Physics-AI workflows for engineering design and diagnostics",
        "System dynamics, measured signals, and computational modeling",
        "Validated tools for design insight, diagnosis, and research outcomes",
    ],
}

EXPERTISE = [
    {
        "title": "Optimization Under Uncertainty",
        "text": "Robust shape optimization, uncertainty quantification, adaptive sampling, and multi-objective design workflows.",
        "icon": "target",
    },
    {
        "title": "Physics-AI and Surrogate Modeling",
        "text": "Physics-informed learning, reduced representations, Gaussian-process surrogates, and data-efficient engineering design.",
        "icon": "brain",
    },
    {
        "title": "Vibroacoustic Simulation",
        "text": "High-frequency acoustic simulation, energy-based methods, and noise reduction for complex engineering systems.",
        "icon": "waves",
    },
    {
        "title": "System Dynamics and Diagnostics",
        "text": "System modeling, frequency-response design, observer-based diagnostics, vibration analysis, and measured-signal interpretation.",
        "icon": "gauge",
    },
    {
        "title": "Control Systems",
        "text": "Classical and embedded control, PID design, estimation, real-time implementation, and automation-system diagnostics.",
        "icon": "sliders",
    },
    {
        "title": "Engineering Software",
        "text": "Scientific Python, GUI applications, open-source APIs, measurement tools, and deployment-ready web demos.",
        "icon": "code",
    },
]

TOOLBOX = [
    "Python",
    "MATLAB",
    "C/C++",
    "NumPy",
    "SciPy",
    "PyTorch",
    "GPyTorch",
    "scikit-learn",
    "Optuna",
    "PySide6",
    "Pymoo",
    "SALib",
    "PyVista",
    "PyGeM",
    "SolidWorks",
    "AutoCAD",
    "Gmsh",
    "COMSOL",
]

EXPERIENCE = [
    {
        "role": "R&D Master Intern - Precision Automation Controls",
        "place": "Western Digital Storage Technologies (Thailand) Ltd.",
        "period": "2018 - 2019",
        "text": "Built data-driven diagnostics from vibration, motor-current, encoder and linear-bearing behavior, and image-derived features for HGA precision-assembly equipment.",
    },
    {
        "role": "Lecturer - Mechanical and Mechatronics",
        "place": "Suranaree University of Technology, Thailand",
        "period": "2019 - 2023",
        "text": "Taught control systems and structural vibration, supervised mechatronics and diagnostics projects, and delivered industrial training in vibration analysis.",
    },
    {
        "role": "PhD Candidate in Mechanical Engineering",
        "place": "Ecole Centrale de Lyon, France",
        "period": "2023 - Present",
        "text": "Research on robust shape optimization under vibroacoustic criteria using surrogate models, uncertainty quantification, and adaptive sampling.",
    },
    {
        "role": "JSPS Short-Term Postdoctoral Fellow",
        "place": "Kyushu University, Japan",
        "period": "2026 - Present",
        "text": "Developing physics-informed autoencoder and graph-neural-network workflows for nonlinear 3D aerodynamic shape reduction and data-efficient surrogate optimization.",
    },
    {
        "role": "Visiting Scientist",
        "place": "AIMR, Tohoku University, Japan",
        "period": "2025",
        "text": "Developed a Physics-AI inverse-design workflow for microscale woven material cells using reduced representations and FEM validation.",
    },
]

FEATURED_PROJECTS = [
    {
        "slug": "pyegro",
        "name": "PyEGRO Library",
        "type": "Open-source optimization library",
        "summary": (
            "Python library for efficient global robust optimization under "
            "uncertainty with adaptive infill, surrogate modeling, and "
            "engineering design workflows."
        ),
        "stack": ["Python", "GPR", "ANN", "Robust Optimization"],
        "status": "Documentation available",
        "href": "https://twanglom.github.io/PyEGRO/",
        "imageUrl": "/software_images/pyegro-demo.png",
        "icon": "library",
    },
    {
        "slug": "mes-acoustic",
        "name": "MES-Acoustic v1.0",
        "type": "Vibroacoustic simulation software",
        "summary": (
            "Software for predicting and optimizing noise in vibroacoustic "
            "environments with clear setup, solving, and visualization workflows."
        ),
        "stack": ["Python", "PySide6", "NumPy", "Acoustics"],
        "status": "Research software",
        "href": "https://github.com/twanglom/MES-Acoustic-Software",
        "imageUrl": "/software_images/MES-Software.png",
        "icon": "volume",
    },
    {
        "slug": "dxf-hatch-pro",
        "name": "DXF Hatch Generator Pro",
        "type": "CAD automation utility",
        "summary": (
            "Desktop tool for generating DXF hatch patterns with image-based "
            "boundary creation and practical CAD-oriented controls."
        ),
        "stack": ["PySide6", "ezdxf", "Matplotlib", "OpenCV"],
        "status": "Required for demo",
        "href": "https://github.com/twanglom/dxf-hatch-gen",
        "imageUrl": "/software_images/dxf-hatch-pro.png",
        "icon": "drafting",
    },
    {
        "slug": "cpr-training-platform",
        "name": "Wireless Platform for Nursing and CPR Training",
        "type": "Educational training system",
        "summary": (
            "Raspberry Pi-based wireless training platform for CPR and nursing "
            "education with real-time feedback and instructor monitoring."
        ),
        "stack": ["Raspberry Pi", "Python", "Bluetooth", "Touch UI"],
        "status": "Download available",
        "imageUrl": "/software_images/cpr_humain_demo.png",
        "downloadUrl": "/downloads/cpr_humain.zip",
        "icon": "heart",
    },
    {
        "slug": "fft-analysis",
        "name": "FFT Analysis Software",
        "type": "Signal processing tool",
        "summary": (
            "Program for vibration sensor interfacing and real-time signal "
            "analysis, applied in educational training sessions."
        ),
        "stack": ["Python", "NumPy", "SciPy", "Tkinter"],
        "status": "Required for demo",
        "imageUrl": "/software_images/fft-analysis-demo.png",
        "icon": "activity",
    },
    {
        "slug": "balancing-system",
        "name": "Balancing System Software v1.2",
        "type": "Rotor balancing tool",
        "summary": (
            "Single-plane rotor balancing tool used in industrial training "
            "programs with monitoring, automated calculations, and reporting."
        ),
        "stack": ["Python", "Qt", "NumPy", "Matplotlib"],
        "status": "Required for demo",
        "imageUrl": "/software_images/Balancing-Software.png",
        "icon": "gauge",
    },
    {
        "slug": "process-control",
        "name": "Process Control Software",
        "type": "Control systems GUI",
        "summary": (
            "GUI-based application for temperature and motor speed control, "
            "PID tuning, live plotting, and classroom demonstrations."
        ),
        "stack": ["Python", "PySide6", "PID", "Control Systems"],
        "status": "Download available",
        "imageUrl": "/software_images/process-control-demo.png",
        "downloadUrl": "/downloads/process-control.zip",
        "icon": "sliders",
    },
    {
        "slug": "measurement-calibration",
        "name": "Measurement and Calibration Software",
        "type": "Instrumentation software",
        "summary": (
            "Measurement acquisition and analog sensor calibration software with "
            "clear workflows for lab and training use."
        ),
        "stack": ["Python", "PySide6", "NumPy", "Calibration"],
        "status": "Download available",
        "imageUrl": "/software_images/measurement-calibration-demo.png",
        "downloadUrl": "/downloads/calibration-software.zip",
        "icon": "ruler",
    },
    {
        "slug": "rotor-ai",
        "name": "RotorAI",
        "type": "Physics-AI demonstration",
        "summary": (
            "A portfolio demo exploring rotor diagnostics through Jeffcott rotor "
            "physics, PINN-based identification, and signal processing."
        ),
        "stack": ["FastAPI", "React", "PyTorch", "PINN"],
        "status": "Live demo",
        "href": "https://rotor-diagnostics.web.app/",
        "imageUrl": "/software_images/rotor-ai-demo.png",
        "localPath": "backup/reference/RotorAI/",
        "icon": "brain",
    },
    {
        "slug": "rotor-digital-twin",
        "name": "Rotor Digital Twin",
        "type": "Digital twin demonstration",
        "summary": (
            "A rotating-machine demo with simulated sensor ingestion, live API "
            "streaming, 3D visualization, and OpenUSD-backed machine state."
        ),
        "stack": ["FastAPI", "React", "Three.js", "OpenUSD"],
        "status": "Live demo",
        "href": "https://rotor-digital-twin.web.app/",
        "imageUrl": "/software_images/rotor-digital-twin-demo.png",
        "localPath": "backup/reference/rotor-digital-twin/",
        "icon": "factory",
    },
]

PUBLICATIONS = [
    {
        "year": 2026,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Shimoyama, K., Gillot, F., & Besset, S. "
            "Robust shape optimization of acoustic diffusers for spatial sound "
            "distribution using Co-Kriging metamodel. Applied Acoustics, 242, 111047. "
            "doi: 10.1016/j.apacoust.2025.111047."
        ),
    },
    {
        "year": 2026,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Gillot, F., Besset, S., and Mahmoudi, S. "
            "AI-assisted symmetry-informed topology optimization of woven materials "
            "for broadband sound absorption. Submitted manuscript."
        ),
    },
    {
        "year": 2025,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Shimoyama, K., Gillot, F., & Besset, S. "
            "Neural-network-based two-stage robust shape optimization for acoustic "
            "noise reduction in an aircraft cabin. Engineering Optimization, 1-19. "
            "doi: 10.1080/0305215X.2025.2563669."
        ),
    },
    {
        "year": 2025,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Gillot, F., & Besset, S. Hybrid Method for "
            "Energy Flow in Mid-High Frequency Acoustics: Applications in "
            "Robust Shape Optimization for Complex Cavities. Journal of "
            "Theoretical and Computational Acoustics. doi: 10.1142/S2591728525500033."
        ),
    },
    {
        "year": 2025,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T., Gillot, F., and Besset, S. A Two-Stage "
            "Metamodeling Approach for Efficient Global Robust Optimization. "
            "DTE 2025 & AICOMAS 2025, Paris, France."
        ),
    },
    {
        "year": 2025,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T. et al. Vibro–Acoustic Modeling of Periodic Woven "
            "Structures Dedicated to Multi-Objective Shape Optimization. "
            "22nd International Conference on Flow Dynamics (ICFD2025), "
            "10–13 November 2025, Sendai, Japan."
        ),
    },
    {
        "year": 2025,
        "kind": "Conference",
        "citation": "Wanglomklang, T. et al. WCSMO 2025, Kobe, Japan.",
    },
    {
        "year": 2026,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T., Shimoyama, K., Besset, S., Gillot, F., and Mahmoudi, S. "
            "Robust Multi-Objective Optimization Design Approaches (Project MuORode). "
            "ELyT Workshop 2026, 7–8 March 2026, Sendai, Japan."
        ),
    },
    {
        "year": 2026,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T. et al. Vibro–Acoustic Modeling of Aircraft Cabin Noise "
            "Induced by Turbulent Boundary Layer Using Radiative Energy Transfer. "
            "17ème Colloque National en Calcul des Structures (CSMA 2026), "
            "18–22 May 2026, Presqu'île de Giens (Var), France."
        ),
    },
    {
        "year": 2024,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T., Gillot, F., and Besset, S. An intersection "
            "interaction hybrid method for energy flow at mid-high frequency "
            "for complex cavities acoustic. ECCOMAS Congress 2024, Lisboa, Portugal."
        ),
    },
    {
        "year": 2022,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T., Tuntavesesak, T., Tumthong, W., and Srisertpol, J. "
            "Artificial neural network-based fault classification of roller bearing "
            "using time responses with observer-based speed control. 6th European "
            "Conference on Electrical Engineering & Computer Science, Bern, Switzerland."
        ),
    },
    {
        "year": 2023,
        "kind": "Journal",
        "citation": (
            "Seangsri, S., Wanglomklang, T., Khaewnak, N., Yachum, N., & "
            "Srisertpol, J. Optimizing Ultra-High Vacuum Control in Electron "
            "Storage Rings Using Fuzzy Control and Estimation of Pumping Speed "
            "by Neural Networks with Molflow+. Systems, 11(3), 116."
        ),
    },
    {
        "year": 2022,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Chommaungpuck, P., Chamniprasart, K., & "
            "Srisertpol, J. Using fault detection and classification techniques "
            "for machine breakdown reduction of the HGA process caused by the "
            "slider loss defect. Manufacturing Review, 9, 21."
        ),
    },
    {
        "year": 2022,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Tuntavesesak, T., Tumthong, W., & Srisertpol, J. "
            "Roller Bearing Faults Classification Using Artificial Neural Network "
            "Based on Servo System with Observer Design. WSEAS Transactions on "
            "Systems, 21, 241-246."
        ),
    },
    {
        "year": 2022,
        "kind": "Journal",
        "citation": (
            "Khaengkarn, S., Nonkeaw, K., Wonglomklang, T., & Srisertpol, J. "
            "Real-Time Tracking and Environmental Monitoring System for Ice Trucks "
            "using IoT Techniques. WSEAS Transactions on Information Science and "
            "Applications, 19, 297-302."
        ),
    },
    {
        "year": 2021,
        "kind": "Journal",
        "citation": (
            "Chommuangpuck, P., Wanglomklang, T., & Srisertpol, J. Fault detection "
            "and diagnosis of linear bearing in auto core adhesion mounting machines "
            "based on condition monitoring. Systems Science & Control Engineering, "
            "9(1), 290-303."
        ),
    },
    {
        "year": 2021,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Chommuangpuck, P., & Srisertpol, J. Energy "
            "Consumption and Vibration of Auto Core Adhesive Mounter Machine in "
            "Case of Linear Bearing Failures. RMUTSB Academic Journal, 7(2), 234-246."
        ),
    },
    {
        "year": 2020,
        "kind": "Journal",
        "citation": (
            "Chommuangpuck, P., Wanglomklang, T., Tantrairatn, S., & Srisertpol, J. "
            "Fault tolerant control based on an observer on PI servo design for a "
            "high-speed automation machine. Machines, 8(2), 22."
        ),
    },
    {
        "year": 2020,
        "kind": "Journal",
        "citation": (
            "Wanglomklang, T., Chommaungpuck, P., & Srisertpol, J. Linear Bearing "
            "Fault Detection Using an Artificial Neural Network Based on a PI Servo "
            "System with the Observer for High-speed Automation Machine. IOP "
            "Conference Series: Materials Science and Engineering, 717(1), 012011."
        ),
    },
    {
        "year": 2020,
        "kind": "Journal",
        "citation": (
            "Thongtan, W., Odngam, S., Wanglomklang, T., & Srisertpol, J. "
            "The Effect of Shaft Whirling on Accuracy of Rotating Coil Magnetic "
            "Measurement System. IOP Conference Series: Materials Science and "
            "Engineering, 717(1), 012012."
        ),
    },
    {
        "year": 2021,
        "kind": "Conference",
        "citation": (
            "Nimthanee, P., Sri-on, T., Wanglomklang, T., and Srisertpol, J. "
            "A wireless monitoring system for cannabis drying chamber. Proceeding "
            "of the 44th Electrical Engineering Conference, Thailand."
        ),
    },
    {
        "year": 2020,
        "kind": "Conference",
        "citation": (
            "Thamcharoen, T., Srisertpol, J., Wanglomklang, T., Chommaungpuck, P., "
            "and Deeying, J. Fault detection and diagnosis via machine learning for "
            "preventing slider loss defect. Conference of Mechanical Engineering "
            "Network of Thailand."
        ),
    },
    {
        "year": 2019,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T., Chommaungpuck, P., and Srisertpol, J. Linear bearing "
            "fault detection using an artificial neural network based on a PI servo "
            "system with the observer for high-speed automation machine. International "
            "Conference on Mechanical, Electronic and Robotics Engineering, Wuhan, China."
        ),
    },
    {
        "year": 2019,
        "kind": "Conference",
        "citation": (
            "Thongtan, W., Odngam, S., Wanglomklang, T., and Srisertpol, J. "
            "The effect of shaft whirling on accuracy of rotating coil magnetic "
            "measurement system. International Conference on Mechanical, Electronic "
            "and Robotics Engineering, Wuhan, China."
        ),
    },
    {
        "year": 2019,
        "kind": "Conference",
        "citation": (
            "Wanglomklang, T., Chommaungpuck, P., and Srisertpol, J. Energy loss "
            "analysis of linear bearing failures in automatic slider attaching process. "
            "15th Conference on Energy Network of Thailand."
        ),
    },
]
