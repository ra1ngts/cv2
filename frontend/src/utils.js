// formateDate
export function formateDate(date) {
    if (!date) return '...';

    const dateObj = new Date(date);

    if (isNaN(dateObj.getTime())) {
        console.error(`Error date formatting: ${date}`);
        return 'Date not found';
    }

    return dateObj.toLocaleDateString('ru-RU', { month: '2-digit', year: 'numeric' }).replace('.', ' / ');
}

// getDuration
export function getDuration(startDate, endDate, isCurrent) {
    const start = formateDate(startDate);
    
    if (isCurrent || !endDate) {
        return `${start} — Present`;
    }
    
    const end = formateDate(endDate);
    return `${start} — ${end}`;
}