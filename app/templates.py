"""HTML templates."""

LANDING = """
<!DOCTYPE html>
<html>
<head>
    <title>Zid SDK Demo</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #fafafa; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .card { background: white; border: 1px solid #e5e5e5; border-radius: 8px; padding: 2.5rem; max-width: 400px; }
        h1 { font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; }
        p { color: #666; margin-bottom: 1.5rem; font-size: 0.9rem; }
        .btn { display: block; background: #000; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none; font-size: 0.9rem; text-align: center; }
        .btn:hover { background: #333; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Zid SDK Demo</h1>
        <p>Connect a Zid store to see the SDK in action.</p>
        <a href="/auth/login" class="btn">Connect Store</a>
    </div>
</body>
</html>
"""

DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - Zid SDK Demo</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #fafafa; padding: 2rem; }
        .container { max-width: 900px; margin: 0 auto; }
        h1 { font-size: 1.25rem; font-weight: 600; margin-bottom: 1.5rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
        .card { background: white; border: 1px solid #e5e5e5; border-radius: 8px; padding: 1.25rem; }
        .card h2 { font-size: 0.75rem; color: #999; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }
        .value { font-size: 1.1rem; font-weight: 500; }
        .sub { color: #666; font-size: 0.85rem; margin-top: 0.25rem; }
        .order-list { list-style: none; }
        .order-item { padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; font-size: 0.9rem; }
        .order-item:last-child { border-bottom: none; }
        .status { font-size: 0.75rem; color: #666; }
        .code { background: #1a1a1a; color: #a3e635; padding: 1.25rem; border-radius: 8px; font-family: 'SF Mono', Monaco, monospace; font-size: 0.8rem; overflow-x: auto; line-height: 1.5; }
        .code .comment { color: #666; }
        .error { color: #dc2626; font-size: 0.9rem; }
        .loading { color: #999; font-size: 0.9rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Dashboard</h1>
        
        <div class="grid">
            <div class="card" id="store-card"><h2>Store</h2><div class="loading">Loading...</div></div>
            <div class="card" id="customers-card"><h2>Customers</h2><div class="loading">Loading...</div></div>
            <div class="card" id="orders-card"><h2>Recent Orders</h2><div class="loading">Loading...</div></div>
        </div>
        
        <div class="code"><span class="comment"># SDK calls powering this page</span>

client.stores.get_profile()
client.customers.list()
client.orders.list()</div>
    </div>
    
    <script>
        async function load() {
            try {
                const store = await fetch('/api/store').then(r => r.json());
                document.getElementById('store-card').innerHTML = `<h2>Store</h2><div class="value">${store.name || store.title || '-'}</div><div class="sub">${store.email || ''}</div>`;
            } catch { document.getElementById('store-card').innerHTML = `<h2>Store</h2><div class="error">Failed to load</div>`; }
            
            try {
                const resp = await fetch('/api/customers').then(r => r.json());
                const count = resp.data?.length || 0;
                document.getElementById('customers-card').innerHTML = `<h2>Customers</h2><div class="value">${count}</div><div class="sub">returned from API</div>`;
            } catch { document.getElementById('customers-card').innerHTML = `<h2>Customers</h2><div class="error">Failed to load</div>`; }
            
            try {
                const resp = await fetch('/api/orders').then(r => r.json());
                const items = (resp.data || []).slice(0, 5).map(o => `<li class="order-item"><span>#${o.id || o.order_id || '-'}</span><span class="status">${o.status || '-'}</span></li>`).join('') || '<li class="order-item">No orders</li>';
                document.getElementById('orders-card').innerHTML = `<h2>Recent Orders</h2><ul class="order-list">${items}</ul>`;
            } catch { document.getElementById('orders-card').innerHTML = `<h2>Recent Orders</h2><div class="error">Failed to load</div>`; }
        }
        load();
    </script>
</body>
</html>
"""
