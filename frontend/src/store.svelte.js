// stateCtx
export const stateCtx = $state({
    profile: {},
    categories: [],
    skills: [],
    experience: [],
    projects: [],
    activeSection: 'about',
    sections: [
        { id: 'about', label: 'About' },
        { id: 'experience', label: 'Experience' },
        { id: 'projects', label: 'Projects' },
        { id: 'contacts', label: 'Contacts' },
    ]
})