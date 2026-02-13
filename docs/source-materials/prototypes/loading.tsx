export default function GlobalLoading() {
  return (
    <section className="loading-skeleton" aria-busy="true" aria-label="Loading content">
      <div className="loading-pulse">
        <div className="loading-bar loading-bar-title" />
        <div className="loading-bar loading-bar-subtitle" />
        <div className="loading-bar loading-bar-body" />
        <div className="loading-bar loading-bar-body short" />
      </div>
    </section>
  );
}
