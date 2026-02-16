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
        .header { margin-bottom: 1.5rem; }
        h1 { font-size: 1.25rem; font-weight: 600; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
        .card { background: white; border: 1px solid #e5e5e5; border-radius: 8px; padding: 1.25rem; }
        .card h2 { font-size: 0.75rem; color: #999; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }
        .value { font-size: 1.1rem; font-weight: 500; }
        .sub { color: #666; font-size: 0.85rem; margin-top: 0.25rem; }
        .order-list { list-style: none; }
        .order-item { padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; font-size: 0.9rem; cursor: pointer; }
        .order-item:hover { background: #f9f9f9; margin: 0 -1.25rem; padding: 0.5rem 1.25rem; }
        .order-item:last-child { border-bottom: none; }
        .status { font-size: 0.75rem; color: #666; }
        .code { background: #1a1a1a; color: #a3e635; padding: 1.25rem; border-radius: 8px; font-family: 'SF Mono', Monaco, monospace; font-size: 0.8rem; overflow-x: auto; line-height: 1.5; }
        .code .comment { color: #666; }
        .error { color: #dc2626; font-size: 0.9rem; }
        .loading { color: #999; font-size: 0.9rem; }
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); align-items: center; justify-content: center; z-index: 100; }
        .modal.active { display: flex; }
        .modal-content { background: white; border-radius: 8px; padding: 1.5rem; max-width: 500px; width: 90%; max-height: 80vh; overflow-y: auto; }
        .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
        .modal-header h3 { font-size: 1rem; font-weight: 600; }
        .modal-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #999; }
        .detail-row { display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #eee; font-size: 0.9rem; }
        .detail-row:last-child { border-bottom: none; }
        .detail-label { color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Dashboard</h1>
        </div>
        
        <div class="grid">
            <div class="card" id="store-card"><h2>Store</h2><div class="loading">Loading...</div></div>
            <div class="card" id="customers-card"><h2>Customers</h2><div class="loading">Loading...</div></div>
            <div class="card" id="orders-card"><h2>Recent Orders</h2><div class="loading">Loading...</div></div>
        </div>
        
        <div class="code"><span class="comment"># Simplified imports - all models at root level</span>
from zid import ZidClient, Order, Customer, Store

client = ZidClient(authorization="...", store_token="...")

<span class="comment"># Typed responses</span>
store: Store = client.stores.get_profile()
customers: list[Customer] = client.customers.list()
orders: list[Order] = client.orders.list()</div>
    </div>
    
    <div class="modal" id="order-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Order Details</h3>
                <button class="modal-close" onclick="closeModal()">&times;</button>
            </div>
            <div id="order-details"></div>
        </div>
    </div>
    
    <script>
        async function load() {
            try {
                const store = await fetch('/api/store').then(r => r.json());
                const s = store.user?.store || store;
                document.getElementById('store-card').innerHTML = `<h2>Store</h2><div class="value">${s.title || s.name || '-'}</div><div class="sub">${s.email || ''}</div>`;
            } catch { document.getElementById('store-card').innerHTML = `<h2>Store</h2><div class="error">Failed to load</div>`; }
            
            try {
                const resp = await fetch('/api/customers').then(r => r.json());
                const count = resp.data?.length || 0;
                document.getElementById('customers-card').innerHTML = `<h2>Customers</h2><div class="value">${count}</div><div class="sub">returned from API</div>`;
            } catch { document.getElementById('customers-card').innerHTML = `<h2>Customers</h2><div class="error">Failed to load</div>`; }
            
            try {
                const resp = await fetch('/api/orders').then(r => r.json());
                const items = (resp.data || []).slice(0, 5).map(o => {
                    const id = o.id || o.order_id || '-';
                    const status = o.order_status?.name || o.status || '-';
                    return `<li class="order-item" onclick="showOrder(${id})"><span>#${id}</span><span class="status">${status}</span></li>`;
                }).join('') || '<li class="order-item">No orders</li>';
                document.getElementById('orders-card').innerHTML = `<h2>Recent Orders</h2><ul class="order-list">${items}</ul>`;
            } catch { document.getElementById('orders-card').innerHTML = `<h2>Recent Orders</h2><div class="error">Failed to load</div>`; }
        }
        
        async function showOrder(id) {
            document.getElementById('order-modal').classList.add('active');
            document.getElementById('order-details').innerHTML = '<div class="loading">Loading...</div>';
            try {
                const order = await fetch(`/api/orders/${id}`).then(r => r.json());
                const o = order.order || order;
                document.getElementById('order-details').innerHTML = `
                    <div class="detail-row"><span class="detail-label">Order ID</span><span>#${o.id || id}</span></div>
                    <div class="detail-row"><span class="detail-label">Status</span><span>${o.order_status?.name || o.status || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Customer</span><span>${o.customer?.name || o.customer_name || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Total</span><span>${o.total_price || o.total || '-'} ${o.currency || ''}</span></div>
                    <div class="detail-row"><span class="detail-label">Payment</span><span>${o.payment_method?.name || o.payment_method || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Created</span><span>${o.created_at || '-'}</span></div>
                `;
            } catch { document.getElementById('order-details').innerHTML = '<div class="error">Failed to load order</div>'; }
        }
        
        function closeModal() { document.getElementById('order-modal').classList.remove('active'); }
        document.getElementById('order-modal').onclick = (e) => { if (e.target.id === 'order-modal') closeModal(); };
        
        load();
    </script>
</body>
</html>
"""
