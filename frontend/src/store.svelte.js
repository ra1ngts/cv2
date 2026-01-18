// stateCtx
export const stateCtx = $state({
    profile: {},
    categories: [],
    skills: [],
    experience: [],
    projects: [],
    form: {},
    contactsData: {
        name: '',
        subject: '',
        message: '',
        email: ''
    },
    formData: new FormData(),
    activeSection: 'about',
    sections: [
        { id: 'about', label: 'About' },
        { id: 'experience', label: 'Experience' },
        { id: 'projects', label: 'Projects' },
        { id: 'contacts', label: 'Contacts' },
    ]
})

export const contactsForm = (form) => {
  form.set('name', stateCtx.contactsData.name || '');
  form.set('subject', stateCtx.contactsData.subject || '');
  form.set('message', stateCtx.contactsData.message || '');
  form.set('email', stateCtx.contactsData.email || '');
  console.log('contactsForm has sent data:', Object.fromEntries(form.entries()));
};