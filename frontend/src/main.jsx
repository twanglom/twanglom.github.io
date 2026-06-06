import React, { useEffect, useMemo, useState } from "react";
import { createRoot } from "react-dom/client";
import {
  Activity,
  ArrowUpRight,
  BookOpen,
  BrainCircuit,
  Code2,
  Cpu,
  Download,
  DraftingCompass,
  Factory,
  Gauge,
  Github,
  GraduationCap,
  HeartPulse,
  Library,
  Mail,
  MapPin,
  Moon,
  Ruler,
  SlidersHorizontal,
  Sun,
  Target,
  Volume2,
  Waves
} from "lucide-react";
import "./styles.css";

const API_BASE = import.meta.env.VITE_API_URL || "";

const fallbackProfile = {
  name: "Thanasak Wanglomklang",
  title: "Mechanical Engineering | Physics-AI Researcher",
  subtitle: "Mechanical engineer connecting system dynamics, measured signals, and computational modeling",
  location: "Fukuoka, Japan",
  email: "thanasak.wang@gmail.com",
  summary:
    "Mechanical engineer and Physics-AI researcher connecting system dynamics, measured signals, and computational modeling to solve practical engineering problems.",
  cvUrl: "/cvfiles/CV-THANASAK-2026.pdf",
  imageUrl: "/profile-1.JPG",
  links: [
    { label: "GitHub", href: "https://github.com/twanglom" },
    { label: "LinkedIn", href: "https://www.linkedin.com/in/thanasak-wanglomklang-6797362aa" },
    { label: "Email", href: "mailto:thanasak.wang@gmail.com" }
  ],
  highlights: [
    "Physics-AI workflows for engineering design and diagnostics",
    "System dynamics, measured signals, and computational modeling",
    "Validated tools for design insight, diagnosis, and research outcomes"
  ],
  expertise: [],
  toolbox: [],
  experience: []
};

const fallbackProjects = [];
const fallbackPublications = [];

const researchHighlights = [
  {
    title: "Physics-Informed Generative Mechanical Part Design",
    eyebrow: "Current Research Highlight",
    summary:
      "Physics-informed graph neural networks for geometric learning, latent-space shape generation, dimensionality reduction, and simulation-aware optimization of mechanical forms.",
    context:
      "The work connects graph-based encoders, generative design, and physics objectives so candidate shapes can be explored in a compact latent space before high-fidelity validation.",
    media: "/research/pi-gnn/pi-gnn-for-generative-mechanical-part-design-animation.mp4",
    poster: "/research/pi-gnn/pi-gnn-for-generative-mechanical-part-design.png",
    image: "/research/pi-gnn/pi-gnn-for-generative-mechanical-part-design.png",
    groundTruth: "/research/pi-gnn/ground-truth.png",
    tags: [
      "PI-GNN",
      "Generative Design",
      "Shape Optimization",
      "Dimensionality Reduction",
      "Geometric Learning"
    ],
    reference: {
      label: "MIT News: AI shapes autonomous underwater gliders",
      href: "https://news.mit.edu/2025/ai-shapes-autonomous-underwater-gliders-0709"
    }
  }
];

const iconMap = {
  activity: Activity,
  brain: BrainCircuit,
  code: Code2,
  cpu: Cpu,
  drafting: DraftingCompass,
  factory: Factory,
  gauge: Gauge,
  graduation: GraduationCap,
  heart: HeartPulse,
  library: Library,
  ruler: Ruler,
  sliders: SlidersHorizontal,
  target: Target,
  volume: Volume2,
  waves: Waves
};

function Icon({ name, size = 20 }) {
  const Component = iconMap[name] || Code2;
  return <Component size={size} strokeWidth={2} />;
}

function usePortfolioData() {
  const [data, setData] = useState({
    profile: fallbackProfile,
    projects: fallbackProjects,
    publications: fallbackPublications,
    apiConnected: false
  });

  useEffect(() => {
    let alive = true;
    Promise.all([
      fetch(`${API_BASE}/api/profile`).then((res) => res.json()),
      fetch(`${API_BASE}/api/projects`).then((res) => res.json()),
      fetch(`${API_BASE}/api/publications`).then((res) => res.json())
    ])
      .then(([profile, projects, publications]) => {
        if (alive) setData({ profile, projects, publications, apiConnected: true });
      })
      .catch(() => {
        if (alive) setData((current) => ({ ...current, apiConnected: false }));
      });
    return () => {
      alive = false;
    };
  }, []);

  return data;
}

function App() {
  const { profile, projects, publications } = usePortfolioData();
  const [theme, setTheme] = useState(() => localStorage.getItem("theme") || "light");

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem("theme", theme);
  }, [theme]);

  const featuredProjects = projects.slice(0, 4);
  const sortedPublications = useMemo(
    () => [...publications].sort((a, b) => b.year - a.year),
    [publications]
  );
  const journalPublications = useMemo(
    () => sortedPublications.filter((p) => p.kind === "Journal"),
    [sortedPublications]
  );
  const conferencePublications = useMemo(
    () => sortedPublications.filter((p) => p.kind === "Conference"),
    [sortedPublications]
  );
  const latestJournal = journalPublications[0];
  const githubLink = profile.links?.find((link) => link.label === "GitHub")?.href || "https://github.com/twanglom";
  const linkedinLink =
    profile.links?.find((link) => link.label === "LinkedIn")?.href ||
    "https://www.linkedin.com/in/thanasak-wanglomklang-6797362aa";

  return (
    <main>
      <nav className="nav">
        <a className="brand" href="#top" aria-label="Home">
          <span className="brandMark">TW</span>
          <span>{profile.name}</span>
        </a>
        <div className="navLinks">
          <a href="#profile">Profile</a>
          <a href="#research">Research</a>
          <a href="#projects">Projects</a>
          <a href="#publications">Publications</a>
          <a href={`mailto:${profile.email}`}>Contact</a>
          <button
            className="iconButton"
            type="button"
            onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
            aria-label="Toggle theme"
            title="Toggle theme"
          >
            {theme === "dark" ? <Sun size={18} /> : <Moon size={18} />}
          </button>
        </div>
      </nav>

      <section id="top" className="hero">
        <div className="heroText">
          <p className="kicker">{profile.title}</p>
          <h1>Mechanical Engineering | Physics-AI Researcher</h1>
          <p className="lede">{profile.summary}</p>
          <div className="heroMeta">
            <span><MapPin size={16} /> {profile.location}</span>
            <span><Mail size={16} /> {profile.email}</span>
          </div>
          <div className="actions">
            <a className="primary" href={profile.cvUrl} target="_blank" rel="noreferrer">
              <Download size={18} /> Download CV
            </a>
            <a className="secondary" href="#projects">
              <ArrowUpRight size={18} /> View Projects
            </a>
            <a className="secondary" href={githubLink} target="_blank" rel="noreferrer">
              <Github size={18} /> GitHub
            </a>
            <a className="secondary" href={linkedinLink} target="_blank" rel="noreferrer">
              <ArrowUpRight size={18} /> LinkedIn
            </a>
          </div>
        </div>

        <aside className="profilePanel" aria-label="Profile summary">
          <img className="profilePhoto" src={profile.imageUrl || "/profile-1.JPG"} alt={profile.name} />
          <div>
            <h2>{profile.name}</h2>
          </div>
        </aside>

        <aside id="research" className="researchNews" aria-label="Current research news">
          {researchHighlights.map((item) => (
            <article className="researchHighlight" key={item.title}>
              <header className="researchHeading">
                <p className="eyebrow">{item.eyebrow}</p>
                <h2>{item.title}</h2>
              </header>
              <div className="researchMediaGrid">
                <figure className="researchMedia">
                  <img src={item.image} alt={`${item.title} overview`} loading="lazy" />
                </figure>
                <figure className="researchMedia researchVideoFrame">
                  <img className="groundTruthImage" src={item.groundTruth} alt="Ground truth mechanical shape" loading="lazy" />
                  <video
                    src={item.media}
                    poster={item.poster}
                    autoPlay
                    muted
                    loop
                    playsInline
                    controls
                  />
                </figure>
              </div>
              <div className="researchCopy">
                <div className="researchText">
                  <p>{item.summary}</p>
                  <p>{item.context}</p>
                </div>
                <div>
                  <div className="tags researchTags">
                    {item.tags.map((tag) => <span key={tag}>{tag}</span>)}
                  </div>
                  <a className="researchReference" href={item.reference.href} target="_blank" rel="noreferrer">
                    <ArrowUpRight size={18} /> {item.reference.label}
                  </a>
                </div>
              </div>
            </article>
          ))}
        </aside>
      </section>

      <section id="profile" className="band">
        <div className="sectionHeader">
          <span>Professional Profile</span>
          <h2>Research depth, engineering tools, and teaching experience.</h2>
        </div>
        <div className="expertiseGrid">
          {profile.expertise?.map((item) => (
            <article className="expertiseItem" key={item.title}>
              <div className="iconTile"><Icon name={item.icon} /></div>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </article>
          ))}
        </div>
        <div className="toolbox">
          <span>Toolbox</span>
          <div>
            {profile.toolbox?.map((tool) => <b key={tool}>{tool}</b>)}
          </div>
        </div>
      </section>

      <section className="section splitSection">
        <div>
          <div className="sectionHeader">
            <span>Experience</span>
            <h2>Industrial experience, academic research, and hands-on training.</h2>
          </div>
        </div>
        <div className="timeline">
          {profile.experience?.map((item) => (
            <article key={`${item.role}-${item.period}`}>
              <span>{item.period}</span>
              <h3>{item.role}</h3>
              <strong>{item.place}</strong>
              <p>{item.text}</p>
            </article>
          ))}
        </div>
      </section>

      <section id="projects" className="section">
        <div className="sectionHeader">
          <span>Featured Projects</span>
          <h2>Engineering software development, user interface, and open-source API.</h2>
        </div>
        <div className="featureStrip">
          {featuredProjects.map((project) => (
            <a className="featureCard" href={project.href || "#projects-list"} key={project.slug}>
              <img src={project.imageUrl} alt={`${project.name} preview`} loading="lazy" />
              <div>
                <span>{project.type}</span>
                <strong>{project.name}</strong>
              </div>
            </a>
          ))}
        </div>
        <div id="projects-list" className="projectGrid">
          {projects.map((project) => (
            <article className="projectCard" key={project.slug}>
              <div className="projectMedia">
                <img src={project.imageUrl} alt={`${project.name} cover`} loading="lazy" />
                <div className="projectIcon"><Icon name={project.icon} size={22} /></div>
              </div>
              <div className="projectBody">
                <p className="eyebrow">{project.type}</p>
                <h3>{project.name}</h3>
                <p>{project.summary}</p>
              </div>
              <div className="tags">
                {project.stack.map((tag) => <span key={tag}>{tag}</span>)}
              </div>
              <div className="projectFooter">
                <small>{project.status}</small>
                <div className="projectActions">
                  {project.downloadUrl ? (
                    <a href={project.downloadUrl} title={`Download ${project.name}`}>
                      <Download size={18} />
                    </a>
                  ) : null}
                  {project.href ? (
                    <a href={project.href} target="_blank" rel="noreferrer" title={`Open ${project.name}`}>
                      <ArrowUpRight size={18} />
                    </a>
                  ) : null}
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section id="publications" className="band publications">
        <div className="sectionHeader">
          <span>Publications</span>
          <h2>Selected journal papers and conference publications.</h2>
        </div>

        <div className="pubGroup">
          <h3 className="pubGroupTitle">Journal Articles</h3>
          {latestJournal ? (
            <div className="publicationLead">
              <BookOpen size={22} />
              <div>
                <strong>{latestJournal.year} · {latestJournal.kind}</strong>
                <p>{latestJournal.citation}</p>
              </div>
            </div>
          ) : null}
          <div className="publicationList">
            {journalPublications.slice(1).map((item) => (
              <article key={`${item.year}-${item.citation}`}>
                <span>{item.year}</span>
                <p>{item.citation}</p>
              </article>
            ))}
          </div>
        </div>

        <div className="pubGroup">
          <h3 className="pubGroupTitle">Presentation in conference</h3>
          <div className="publicationList">
            {conferencePublications.map((item) => (
              <article key={`${item.year}-${item.citation}`}>
                <span>{item.year}</span>
                <p>{item.citation}</p>
              </article>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
