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
        .container { max-width: 1100px; margin: 0 auto; }
        .header { margin-bottom: 1.5rem; }
        h1 { font-size: 1.25rem; font-weight: 600; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
        .card { background: white; border: 1px solid #e5e5e5; border-radius: 8px; padding: 1.25rem; }
        .card.wide { grid-column: span 2; }
        .card h2 { font-size: 0.75rem; color: #999; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }
        .value { font-size: 1.1rem; font-weight: 500; }
        .sub { color: #666; font-size: 0.85rem; margin-top: 0.25rem; }
        .item-list { list-style: none; }
        .item { padding: 0.5rem 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; font-size: 0.9rem; cursor: pointer; }
        .item:hover { background: #f9f9f9; margin: 0 -1.25rem; padding: 0.5rem 1.25rem; }
        .item:last-child { border-bottom: none; }
        .item-info { display: flex; flex-direction: column; gap: 2px; }
        .item-name { font-weight: 500; }
        .item-sub { font-size: 0.8rem; color: #666; }
        .badge { font-size: 0.7rem; padding: 0.2rem 0.5rem; border-radius: 4px; background: #e5e5e5; color: #666; }
        .badge.success { background: #dcfce7; color: #166534; }
        .badge.warning { background: #fef3c7; color: #92400e; }
        .badge.info { background: #dbeafe; color: #1e40af; }
        .store-details { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; }
        .store-row { display: flex; justify-content: space-between; font-size: 0.85rem; padding: 0.3rem 0; }
        .store-label { color: #666; }
        .error { color: #dc2626; font-size: 0.9rem; }
        .loading { color: #999; font-size: 0.9rem; }
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); align-items: center; justify-content: center; z-index: 100; }
        .modal.active { display: flex; }
        .modal-content { background: white; border-radius: 8px; padding: 1.5rem; max-width: 550px; width: 90%; max-height: 80vh; overflow-y: auto; }
        .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
        .modal-header h3 { font-size: 1rem; font-weight: 600; }
        .modal-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #999; }
        .detail-row { display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #eee; font-size: 0.9rem; }
        .detail-row:last-child { border-bottom: none; }
        .detail-label { color: #666; }
        .section-title { font-size: 0.8rem; color: #999; text-transform: uppercase; margin-top: 1rem; margin-bottom: 0.5rem; padding-top: 0.5rem; border-top: 1px solid #eee; }
        .product-item { display: flex; justify-content: space-between; font-size: 0.85rem; padding: 0.3rem 0; }
        .token-box { background: #f5f5f5; border: 1px solid #e5e5e5; border-radius: 6px; padding: 0.75rem; margin-top: 0.5rem; font-family: 'Courier New', monospace; font-size: 0.8rem; word-break: break-all; position: relative; }
        .token-label { font-size: 0.75rem; color: #666; margin-bottom: 0.25rem; font-weight: 600; }
        .copy-btn { position: absolute; top: 0.5rem; right: 0.5rem; background: white; border: 1px solid #ddd; border-radius: 4px; padding: 0.25rem 0.5rem; font-size: 0.7rem; cursor: pointer; color: #666; }
        .copy-btn:hover { background: #f9f9f9; border-color: #999; }
        .copy-btn.copied { background: #dcfce7; color: #166534; border-color: #86efac; }
        @media (max-width: 768px) { .card.wide { grid-column: span 1; } .store-details { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Dashboard</h1>
        </div>
        
        <div class="grid">
            <div class="card wide" id="store-card"><h2>Store Info</h2><div class="loading">Loading...</div></div>
            <div class="card" id="products-card"><h2>Products</h2><div class="loading">Loading...</div></div>
            <div class="card" id="customers-card"><h2>Customers</h2><div class="loading">Loading...</div></div>
            <div class="card" id="orders-card"><h2>Recent Orders</h2><div class="loading">Loading...</div></div>
            <div class="card" id="webhooks-card"><h2>Webhooks</h2><div class="loading">Loading...</div></div>
            <div class="card wide" id="tokens-card"><h2>API Tokens</h2><div class="loading">Loading...</div></div>
        </div>
    </div>
    
    <div class="modal" id="detail-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modal-title">Details</h3>
                <button class="modal-close" onclick="closeModal()">&times;</button>
            </div>
            <div id="modal-body"></div>
        </div>
    </div>
    
    <script>
        async function load() {
            // Tokens
            try {
                const tokens = await fetch('/api/tokens').then(r => r.json());
                document.getElementById('tokens-card').innerHTML = `
                    <h2>API Tokens</h2>
                    <div class="sub" style="margin-bottom: 0.75rem">Use these tokens for testing API calls</div>
                    <div style="position: relative;">
                        <div class="token-label">Authorization Token (Bearer)</div>
                        <div class="token-box" id="auth-token">${tokens.authorization_token || 'Not available'}
                            <button class="copy-btn" onclick="copyToken('auth-token', this)">Copy</button>
                        </div>
                    </div>
                    <div style="position: relative; margin-top: 1rem;">
                        <div class="token-label">Access Token (X-Manager-Token)</div>
                        <div class="token-box" id="access-token">${tokens.access_token || 'Not available'}
                            <button class="copy-btn" onclick="copyToken('access-token', this)">Copy</button>
                        </div>
                    </div>`;
            } catch { document.getElementById('tokens-card').innerHTML = `<h2>API Tokens</h2><div class="error">Failed to load tokens</div>`; }
            
            // Store info
            try {
                const store = await fetch('/api/store').then(r => r.json());
                const s = store.user?.store || store;
                document.getElementById('store-card').innerHTML = `
                    <h2>Store Info</h2>
                    <div class="value">${s.title || '-'}</div>
                    <div class="sub" style="margin-bottom: 1rem">${s.username || ''}</div>
                    <div class="store-details">
                        <div class="store-row"><span class="store-label">ID</span><span>${s.id || '-'}</span></div>
                        <div class="store-row"><span class="store-label">Email</span><span>${s.email || '-'}</span></div>
                        <div class="store-row"><span class="store-label">Phone</span><span>${s.phone || '-'}</span></div>
                        <div class="store-row"><span class="store-label">Country</span><span>${s.currency?.country?.name || '-'}</span></div>
                        <div class="store-row"><span class="store-label">Currency</span><span>${s.currency?.code || '-'}</span></div>
                        <div class="store-row"><span class="store-label">Plan</span><span>${s.subscription?.package_name?.en || s.subscription?.package_code || '-'}</span></div>
                    </div>`;
            } catch { document.getElementById('store-card').innerHTML = `<h2>Store Info</h2><div class="error">Failed to load</div>`; }
            
            // Products
            try {
                const resp = await fetch('/api/products').then(r => r.json());
                const products = resp.data || [];
                const items = products.slice(0, 6).map(p => `
                    <li class="item">
                        <div class="item-info">
                            <span class="item-name">${p.name?.en || p.name?.ar || '-'}</span>
                            <span class="item-sub">SKU: ${p.sku || '-'}</span>
                        </div>
                        <span class="badge">${p.price != null ? p.price + ' ' + (p.currency || '') : '-'}</span>
                    </li>`).join('') || '<li class="item"><span class="item-sub">No products</span></li>';
                document.getElementById('products-card').innerHTML = `
                    <h2>Products <span style="color:#666;font-weight:normal">(${products.length})</span></h2>
                    <ul class="item-list">${items}</ul>`;
            } catch { document.getElementById('products-card').innerHTML = `<h2>Products</h2><div class="error">Failed to load</div>`; }

            // Customers
            try {
                const resp = await fetch('/api/customers').then(r => r.json());
                const customers = resp.data || [];
                const items = customers.slice(0, 6).map(c => `
                    <li class="item" onclick='showCustomer(${JSON.stringify(c).replace(/'/g, "\\'")})'>
                        <div class="item-info">
                            <span class="item-name">${c.name || c.first_name || 'Unknown'}</span>
                            <span class="item-sub">${c.email || c.mobile || '-'}</span>
                        </div>
                        <span class="badge info">${c.orders_count || 0} orders</span>
                    </li>`).join('') || '<li class="item">No customers</li>';
                document.getElementById('customers-card').innerHTML = `
                    <h2>Customers <span style="color:#666;font-weight:normal">(${customers.length})</span></h2>
                    <ul class="item-list">${items}</ul>`;
            } catch { document.getElementById('customers-card').innerHTML = `<h2>Customers</h2><div class="error">Failed to load</div>`; }
            
            // Orders
            try {
                const resp = await fetch('/api/orders').then(r => r.json());
                const orders = resp.data || [];
                const items = orders.slice(0, 6).map(o => {
                    const id = o.id || o.order_id || '-';
                    const status = o.order_status?.name || o.status || '-';
                    const statusClass = status.toLowerCase().includes('complete') ? 'success' : status.toLowerCase().includes('pending') ? 'warning' : '';
                    return `<li class="item" onclick="showOrder(${id})">
                        <div class="item-info">
                            <span class="item-name">#${id}</span>
                            <span class="item-sub">${o.customer?.name || o.customer_name || '-'}</span>
                        </div>
                        <span class="badge ${statusClass}">${status}</span>
                    </li>`;
                }).join('') || '<li class="item">No orders</li>';
                document.getElementById('orders-card').innerHTML = `
                    <h2>Recent Orders <span style="color:#666;font-weight:normal">(${orders.length})</span></h2>
                    <ul class="item-list">${items}</ul>`;
            } catch { document.getElementById('orders-card').innerHTML = `<h2>Recent Orders</h2><div class="error">Failed to load</div>`; }
            
            // Webhooks
            try {
                const resp = await fetch('/api/webhooks').then(r => r.json());
                const webhooks = resp.data || [];
                const items = webhooks.slice(0, 5).map(w => `
                    <li class="item" onclick='showWebhook(${JSON.stringify(w).replace(/'/g, "\\'")})'>
                        <div class="item-info">
                            <span class="item-name">${w.event || '-'}</span>
                            <span class="item-sub">${w.target_url || '-'}</span>
                        </div>
                    </li>`).join('') || '<li class="item">No webhooks configured</li>';
                document.getElementById('webhooks-card').innerHTML = `
                    <h2>Webhooks <span style="color:#666;font-weight:normal">(${webhooks.length})</span></h2>
                    <ul class="item-list">${items}</ul>`;
            } catch { document.getElementById('webhooks-card').innerHTML = `<h2>Webhooks</h2><div class="error">Failed to load</div>`; }
        }
        
        function showModal(title, content) {
            document.getElementById('modal-title').textContent = title;
            document.getElementById('modal-body').innerHTML = content;
            document.getElementById('detail-modal').classList.add('active');
        }
        
        function closeModal() { document.getElementById('detail-modal').classList.remove('active'); }
        document.getElementById('detail-modal').onclick = (e) => { if (e.target.id === 'detail-modal') closeModal(); }
        
        function copyToken(elementId, btn) {
            const element = document.getElementById(elementId);
            const text = element.textContent.replace('Copy', '').trim();
            navigator.clipboard.writeText(text).then(() => {
                btn.textContent = 'Copied!';
                btn.classList.add('copied');
                setTimeout(() => {
                    btn.textContent = 'Copy';
                    btn.classList.remove('copied');
                }, 2000);
            });
        };
        
        function showCustomer(c) {
            showModal('Customer Details', `
                <div class="detail-row"><span class="detail-label">Name</span><span>${c.name || c.first_name || '-'} ${c.last_name || ''}</span></div>
                <div class="detail-row"><span class="detail-label">Email</span><span>${c.email || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Phone</span><span>${c.mobile || c.phone || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">City</span><span>${c.city?.name || c.city || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Country</span><span>${c.country?.name || c.country || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Total Orders</span><span>${c.orders_count || 0}</span></div>
                <div class="detail-row"><span class="detail-label">Total Spent</span><span>${c.total_spent || c.total_orders_amount || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Created</span><span>${c.created_at || '-'}</span></div>
            `);
        }
        
        async function showOrder(id) {
            showModal('Order Details', '<div class="loading">Loading...</div>');
            try {
                const order = await fetch('/api/orders/' + id).then(r => r.json());
                const o = order.order || order;
                const products = (o.products || o.items || []).map(p => `
                    <div class="product-item">
                        <span>${p.name || p.product_name || '-'} x${p.quantity || 1}</span>
                        <span>${p.price || '-'}</span>
                    </div>`).join('') || '<div class="item-sub">No products</div>';
                
                document.getElementById('modal-body').innerHTML = `
                    <div class="detail-row"><span class="detail-label">Order ID</span><span>#${o.id || id}</span></div>
                    <div class="detail-row"><span class="detail-label">Status</span><span>${o.order_status?.name || o.status || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Customer</span><span>${o.customer?.name || o.customer_name || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Email</span><span>${o.customer?.email || o.email || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Phone</span><span>${o.customer?.mobile || o.phone || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Subtotal</span><span>${o.sub_total || '-'} ${o.currency || ''}</span></div>
                    <div class="detail-row"><span class="detail-label">Shipping</span><span>${o.shipping?.cost || o.shipping_cost || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Total</span><span>${o.total_price || o.total || '-'} ${o.currency || ''}</span></div>
                    <div class="detail-row"><span class="detail-label">Payment</span><span>${o.payment_method?.name || o.payment_method || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">Created</span><span>${o.created_at || '-'}</span></div>
                    <div class="section-title">Products</div>
                    ${products}
                    <div class="section-title">Shipping Address</div>
                    <div class="detail-row"><span class="detail-label">Address</span><span>${o.address?.street || o.shipping_address || '-'}</span></div>
                    <div class="detail-row"><span class="detail-label">City</span><span>${o.address?.city?.name || o.city || '-'}</span></div>
                `;
            } catch { document.getElementById('modal-body').innerHTML = '<div class="error">Failed to load order</div>'; }
        }
        
        function showWebhook(w) {
            showModal('Webhook Details', `
                <div class="detail-row"><span class="detail-label">ID</span><span>${w.id || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Event</span><span>${w.event || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Target URL</span><span style="word-break:break-all">${w.target_url || '-'}</span></div>
                <div class="detail-row"><span class="detail-label">Created</span><span>${w.created_at || '-'}</span></div>
            `);
        }
        
        load();
    </script>
</body>
</html>
"""
