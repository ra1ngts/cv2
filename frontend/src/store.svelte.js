// stateCtx
export const stateCtx = $state({
    profile: {},
    categories: [],
    skills: [],
    frontendSkills: [],
    backendSkills: [],
    experience: [],
    projects: [],
    form: {},
    contactsData: {
        name: '',
        subject: '',
        message: '',
        email: ''
    },
    formErrors: {},
    touchedFields: {},
    activeSection: 'about',
    sections: [
        { id: 'about', label: 'About' },
        { id: 'experience', label: 'Experience' },
        { id: 'projects', label: 'Projects' },
        { id: 'contacts', label: 'Contacts' },
    ]
})

export const contactsForm = () => {
  const form = new FormData();
  form.set('name', stateCtx.contactsData.name || '');
  form.set('subject', stateCtx.contactsData.subject || '');
  form.set('message', stateCtx.contactsData.message || '');
  form.set('email', stateCtx.contactsData.email || '');
  console.log('contactsForm has sent data:', Object.fromEntries(form.entries()));
  return form;
};